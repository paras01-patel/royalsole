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
        return redirect('login')

    return render(req, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

            if user.check_password(password):
                request.session["username"] = user.username
                messages.success(request, "Login Successfully")
                return redirect("home")
            else:
                messages.error(request, "Wrong Password")
                return redirect("login")

        except User.DoesNotExist:
            messages.error(request, "User Not Found")
            return redirect("login")

    return render(request, "login.html")


def logout(req):
    req.session.flush()
    messages.success(req,'logout successfully')
    return render(req,'login.html')
