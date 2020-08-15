from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView, EditProfilePageView, CreateProfilePageView
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'user_auth'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-settings/', UserEditView.as_view(), name='edit_settings'),
    path('password/', PasswordChangeView.as_view(), name='edit_password'),
    path('password-success/', password_success, name="password-success"),
    path('<int:pk>/profile/', profile_page, name="profile"),
    path('<int:pk>/edit-profile/', EditProfilePageView.as_view(), name="edit_profile"),
    path('create-profile-page/', CreateProfilePageView.as_view(), name="create_profile"),
    path('test/', test)
]
