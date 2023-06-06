from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog



def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})



def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    template_name = f"blogs/{blog.blog_title.replace(' ', '_').lower()}.html"
    return render(request, template_name, {'blog': blog})
