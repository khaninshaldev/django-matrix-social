from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/new', views.newPost, name="new"),
    path('posts/<int:pk>', views.getPost, name="details"),
    path('posts/<int:pk>/edit', views.editPost, name="edit"),
    path('posts/<int:pk>/delete', views.deletePost, name="delete"),
]
