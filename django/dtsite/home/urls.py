from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('login', views.handleLogin, name='handleLogin'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('logout', views.handleLogout, name='handleLogout')

    
]


