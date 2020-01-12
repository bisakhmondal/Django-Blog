from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin, # to redirect is not logged in
UserPassesTestMixin)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'home'
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'#<app>/<model>_<view>.html
    context_object_name='posts'
    ordering=['-date_posted'] #- for reverse
    paginate_by=8

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_home.html'#<app>/<model>_<view>.html
    context_object_name='posts'
    #ordering=['-date_posted'] #- for reverse
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    #success_url='' if you wan to redirect to another page
    fields=['title','contents']

    #overide form_valid method to let createview know who is the user
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    success_url='/' #if you wan to redirect to another page
    fields=['title','contents']

    #overide form_valid method to let createview know who is the user
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
#remind deleteview and detail view are nearly similar and updateview and create view are nearly similar
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    context_object_name='post'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
def about(request):
    return render(request,'blog/about.html',{'title':'about'})
