from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.index, name='index'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('add-post', views.AddPostView.as_view(), name='add-post')
]