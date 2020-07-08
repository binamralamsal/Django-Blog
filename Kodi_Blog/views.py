from django.shortcuts import render
from Blog.models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blog': blogs})