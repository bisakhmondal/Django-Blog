from django.urls import path
from .import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AnnouncementListView
)

urlpatterns=[
    path('',PostListView.as_view(),name='blog_home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user_post'),
    path('post/<int:pk>/comment/new/',views.add_comment_to_post,name='comment_create'),
    path('user/<str:username>',UserPostListView.as_view(),name='user_post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
    path('about/',views.about,name='blog_about'),
    path('anouncements/',AnnouncementListView.as_view(),name='blog_announcements')


]


