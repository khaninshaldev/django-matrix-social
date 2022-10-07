from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new', views.newPost, name="new"),
    path('<int:pk>', views.getPost, name="details"),
    path('<int:pk>/edit', views.editPost, name="edit"),
    path('<int:pk>/delete', views.deletePost, name="delete"),
]
