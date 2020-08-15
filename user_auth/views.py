from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm, EditProfilePageForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
# from django.contrib.auth.forms import PasswordChangeForm
from Blog.models import Profile, Post


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def test(request):
    return render(request, 'registration/login_new.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

    else:
        return reverse_lazy('blog:home')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('blog:home')

    def get_object(self):
        return self.request.user


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('user_auth:password-success')


def password_success(request):
    return render(request, 'registration/password-success.html')


def profile_page(request, pk):
    profile = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(author_id=pk)
    return render(request, 'registration/profile.html', {'profile': profile, 'posts': posts})


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    form_class = EditProfilePageForm
    # fields = ['bio', 'profile_pic', 'website_url', 'facebook', 'twitter', 'instagram', 'youtube', 'pinterest',
    #           'telegram']
    success_url = reverse_lazy('blog:home')


class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
