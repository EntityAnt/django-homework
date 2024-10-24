from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView, ContactView,
)

app_name = 'blog'

urlpatterns = [
    path('post/', BlogPostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),
    path('contact/', ContactView.as_view(), name='blog_contact'),
]
