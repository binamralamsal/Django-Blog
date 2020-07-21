from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title', 'description', 'author', 'browser_title', 'slug', 'excerpt', 'category')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title here...'}),
            'browser_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title to show in browser here... Leave blank to show blog title as browser title'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your description here...'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your slug here without spaces that will be url of your blog...'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your excerpt here...'}),
            'category': forms.CheckboxSelectMultiple(attrs={"style": "list-style:none;"})
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title', 'description', 'browser_title', 'slug', 'excerpt', 'category')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'browser_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your excerpt here...'}),
            'category': forms.CheckboxSelectMultiple(attrs={})

        }
