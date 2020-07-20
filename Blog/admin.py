from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'id', 'category', 'date_published', 'author', 'slug')
    list_filter = ('category',)
    search_fields = ('blog_title', 'date_published')
    prepopulated_fields = {'slug': ('blog_title',)}

    fieldsets = (
        (None, {
            'fields': ('blog_title', 'description', 'category', 'author')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_published', 'browser_title', 'slug', 'excerpt'),
        }),
    )


# Register your models here.
admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)