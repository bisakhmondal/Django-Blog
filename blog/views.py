from django.shortcuts import render

posts=[
    {
        'title':'Blog Post 1',
        'author':'Bisakh Mondal',
        'date':'8th Jan,2020',
        'content':'first blog post'
    },
    {
        'title':'Blog Post 2',
        'author':'jane doe',
        'date':'9th Jan,2020',
        'content':'second blog post'
    }
]
# Create your views here.
def home(request):
    context={
        'posts':posts,
        'title':'home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
