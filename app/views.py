from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def home(req):
    return render(req, 'home.html')


def signup(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')

        if password1 != password2:
            messages.error(req, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(req, 'Username already exists')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(req, 'Email already exists')
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(req, 'Signup Successfully')
        return redirect('home')

    return render(req, 'signup.html')