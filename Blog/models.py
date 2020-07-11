from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=300)
    browser_title = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    date_published = models.DateField(default=timezone.now)
    ordering_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        print(self.id)
        return reverse('blog:home')


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
