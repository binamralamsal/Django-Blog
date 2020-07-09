from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def home(request):
    blogs = Post.objects.all()
    return render(request, 'blog/home.html', {'blog': blogs})


def detail(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    if blog.browser_title == "":
        blog.browser_title = blog.blog_title
    return render(request, 'blog/detail.html', {'Blog': blog})


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/Add Post.html'
    fields = "__all__"
