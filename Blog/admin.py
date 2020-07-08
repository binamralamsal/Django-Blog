from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'id', 'category', 'date_published')
    list_filter = ('category',)
    search_fields = ('blog_title', 'date_published')

    fieldsets = (
        (None, {
            'fields': ('blog_title', 'description', 'category')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_published',),
        }),
    )


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)