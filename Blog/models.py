from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.blog_title
    blog_title = models.CharField(max_length=300)
    description = models.TextField(default="")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_published = models.DateField(default=timezone.now)


class Category(models.Model):
    def __str__(self):
        return self.category
    category = models.CharField(max_length=50)