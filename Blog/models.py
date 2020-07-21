from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, default="")

    def __str__(self):
        return self.category


# Create your models here.
# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=300)
    browser_title = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")
    date_published = models.DateField(default=timezone.now)
    ordering_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='date_published')
    excerpt = models.TextField(max_length=200, default="", blank=True)
    likes = models.ManyToManyField(User, related_name="blog_posts", blank=True)
    category = models.ManyToManyField(Category, related_name="categories")

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        print(self.id)
        return reverse('blog:home')
