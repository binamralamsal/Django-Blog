from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.BlogIndex.as_view(), name='index'),
    path('blog/<str:slug>/<int:pk>', views.post_detail, name='detail'),
    path('add-post', views.AddPostView.as_view(), name='add-post'),
    path('edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('category/<str:cat_slug>/', views.category, name='category'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('comment/', views.post_comment, name='postcomment'),
]