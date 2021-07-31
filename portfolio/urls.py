"""URL for Portfolio app"""

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Home page for portfolio app
    path('', views.home, name='home'),
]