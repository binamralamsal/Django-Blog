from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='index'),
    path('blog/', views.index, name='index'),
    path('blog/<int:blog_id>/', views.detail, name='detail')
]