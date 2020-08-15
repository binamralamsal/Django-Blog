from django.contrib import admin
from .models import Post, Category, Profile, Comment


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
            'fields': ('blog_title', 'description', 'author', 'category', 'excerpt', 'featured_image')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_published', 'browser_title', 'slug', 'likes', 'tags'),
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user',)


# Register your models here.
admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
