from django.shortcuts import render

from .models import Project

# Create your views here.
def home(request):
    """Home page for Portfolio app"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/home.html', context)