from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginAuth, name="login"),
    path('register', views.registerAuth, name="register"),
    path('logout', views.logoutAuth, name="logout"),
]
