from django.contrib import messages
from django.contrib.auth.decorators import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from .models import Category, Comment
from django.http import HttpResponseRedirect


def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:detail', args=[post.slug, post.pk]))


class BlogIndex(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-ordering_date']


# class HomeView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     ordering = ['-ordering_date']

def home(request):
    posts = Post.objects.all()
    programming = Category.objects.get(category='Programming')
    entertainment = Category.objects.get(category='Entertainment')
    health = Category.objects.get(category='Health')
    education = Category.objects.get(category='Education')
    programming = Post.objects.filter(category=programming.id)
    entertainment = Post.objects.filter(category=entertainment.id)
    front_post3 = Post.objects.filter(category=health.id)
    education = Post.objects.filter(category=education.id)
    context = {
        'posts': posts,
        'programming': programming,
        'entertainment': entertainment,
        'front_post3': front_post3,
        'education': education
    }

    return render(request, 'blog/home.html', context)


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'

def post_detail(request, slug, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    similar_post = Post.objects.filter(category=post.category.all()[0].id)
    size = 4
    if len(similar_post) < 4:
        size = len(similar_post.all())

    tags = post.tags.split(',')
    if tags[0] == '' and len(tags) <= 1:
        tags = None
    print(tags)
    recent_posts = Post.objects.all()[:2]
    context = {
        'post': post,
        'similar_post': similar_post.all()[:size],
        'tags': tags,
        'recent_posts': recent_posts,
        'comments': comments
    }
    return render(request, 'blog/detail.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


def category(request, cat_slug):
    categories = Category.objects.get(slug=cat_slug)
    category_posts = Post.objects.filter(category=categories.id).reverse()
    arguments = {
        'category': category_posts,
        'category_name': categories.category
    }
    return render(request, 'blog/categories.html', arguments)


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'


def delete_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("blog:home")


@login_required(login_url='login')
def post_comment(request):
    if request.method == "POST":
        postID = request.POST.get("postID")
        post = Post.objects.get(id=postID)
        body = request.POST.get("comment")

        if request.user.is_authenticated:
            user = request.user.profile
            comment = Comment(post=post, user=user, body=body, )
            comment.save()
        else:
            comment = Comment()
        messages.success(request, "Your comment has been posted succesfully")
    return redirect('blog:detail', post.slug, post.id)
