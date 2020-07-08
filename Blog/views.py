from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def home(request):
    blogs = Post.objects.all()
    return render(request, 'blog/home.html', {'blog': blogs})


def detail(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', {'Blog': blog})
