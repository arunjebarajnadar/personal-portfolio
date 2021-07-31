from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Blog

# Create your views here.
def all_blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    """Show blog details"""
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/detail.html', context)