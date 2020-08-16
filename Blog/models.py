from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField, ImageCropField


class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, default="")

    def __str__(self):
        return self.category


# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=300)
    browser_title = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, upload_to="images/", default='blog/images/author'
                                                                                           '.png')
    cropping = ImageRatioField('featured_image', '750x450')
    date_published = models.DateField(default=timezone.now)
    ordering_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250)
    excerpt = models.TextField(max_length=200, default="")
    likes = models.ManyToManyField(User, related_name="blog_posts", blank=True)
    category = models.ManyToManyField(Category, related_name="categories")
    tags = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        print(self.id)
        return reverse('blog:home')

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.featured_image.path)
        if img.height > 450 or img.width > 750:
            output_size = (750, 450)
            img.thumbnail(output_size)
            img.save(self.featured_image.path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="images/profile/", null=True, blank=True, default="blog/images"
                                                                                                "/author.png")
    website_url = models.URLField(max_length=255, null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    youtube = models.URLField(max_length=255, null=True, blank=True)
    telegram = models.URLField(max_length=255, null=True, blank=True)
    pinterest = models.URLField(max_length=255, null=True, blank=True)
    verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        print(self.id)
        return reverse('blog:home')

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    post = models.OneToOneField(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    replies = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="comment_like", blank=True)

    def __str__(self):
        return self.body
