from django.shortcuts import render, HttpResponse
from django.contrib import auth
# Create your views here.

def home(request):
    return render(request, 'index.html', {'username': auth.get_user(request)})