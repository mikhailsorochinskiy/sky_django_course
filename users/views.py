from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserRegisterForm
from .models import User
from django.urls import reverse_lazy

# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('catalog:home')

