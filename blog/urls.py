from django.urls import path
from .import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView
    )

urlpatterns=[
    path('',PostListView.as_view(),name='blog_home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/comment/new/',CommentCreateView.as_view(),name='comment_create'),
    path('post/<int:pk>/comment/<int:pk1>/update/',PostUpdateView.as_view(),name='comment_update'),
    path('post/<int:pk>/comment/<int:pk1>/delete/',PostUpdateView.as_view(),name='comment_delete'),
    
    path('about/',views.about,name='blog_about')


]


