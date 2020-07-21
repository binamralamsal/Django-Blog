from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy
from .models import Category


class BlogIndex(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-ordering_date']


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-ordering_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


def CategoryView(request, cat_slug):
    categories = Category.objects.get(slug=cat_slug)
    category_posts = Post.objects.filter(category=categories.id).reverse()

    return render(request, 'blog/categories.html', {'category': category_posts, 'category_name': categories.category})


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = 'blog/delete_post.html'
