from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm
# Create your views here.

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'index.html')
    return render(request, "form.html", {"form": form})


def reqister_view(request):
    return render(request, "form.html", {})


def logout_view(request):
    return render(request, "form.html", {})