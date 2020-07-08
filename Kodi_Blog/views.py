from django.shortcuts import render
from Blog.models import Blog


def home(request):
    blog = (Blog.objects.all())
    return render(request, 'home.html', {'blog': blog})