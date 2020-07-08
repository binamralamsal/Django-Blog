from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="blog_index"),
    path('blog/', views.index, name="blog_index"),
    path('blog/<int:blog_id>/', views.detail, name="blog_detail")
]