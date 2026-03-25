from django.shortcuts import render, redirect

from user_auth.models import UserAuthModel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                 userinfo = UserAuthModel.objects.create(
                      username=username,
                     full_name = full_name,
                     email = email,
                     contact_number = contact,
                     password =(password),
                     
                 )
                 userinfo.save()
                 return redirect('login')
            else:
                 messages.error(request, 'password do not match')
                 

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')