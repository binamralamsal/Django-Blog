from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'id', 'date_published', 'author', 'slug')
    list_filter = ('category',)
    search_fields = ('blog_title', 'date_published')
    prepopulated_fields = {'slug': ('blog_title',)}

    fieldsets = (
        (None, {
            'fields': ('blog_title', 'description', 'author', 'category')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_published', 'browser_title', 'slug', 'excerpt', 'likes'),
        }),
    )


# Register your models here.
admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)