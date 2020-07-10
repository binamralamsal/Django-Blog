from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title', 'description', 'category', 'author', 'browser_title')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'browser_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title', 'description', 'category', 'browser_title')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'browser_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
