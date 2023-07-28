from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.welcome,name='welcome'),
    path('signup', views.Signup,name='Signup'),
    path('', views.Login,name='Login'),
    path('login', views.Login,name='Login'),
    path('index', views.index,name='index'),
    path('logout', views.LogoutPage,name='logout'),
    path('user-profile', views.userprofile,name='user-profile'),
    path('savechanges', views.savechanges,name='savechanges'),
    
]