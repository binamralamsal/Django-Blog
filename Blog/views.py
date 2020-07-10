from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'blog/index.html')


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-id']


def detail(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    if blog.browser_title == "":
        blog.browser_title = blog.blog_title
    return render(request, 'blog/detail.html', {'Blog': blog})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = 'blog/delete_post.html'
