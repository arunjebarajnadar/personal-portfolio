"""Defines URL Patterns for blog"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home Page for blog
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]