from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.index, name='index'),
    path('blog/<str:slug>/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('add-post', views.AddPostView.as_view(), name='add-post'),
    path('edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
]