from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"


class LoginView(TemplateView):
    template_name="user_login.html"
