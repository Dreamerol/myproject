from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from bookapp.accounts.forms import UserCreateForm

#

# Create your views here.

class SignInView(auth_views.LoginView):
    template_name = 'login-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')


class SignUpView(views.CreateView):
    template_name = 'register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

class SignOutView():
    pass