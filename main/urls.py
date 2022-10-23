from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name="auth"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('main', views.main, name="main"),
]