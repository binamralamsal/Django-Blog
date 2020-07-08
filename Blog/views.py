from django.shortcuts import render
from .models import Blog


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', {'Blog': blog})
