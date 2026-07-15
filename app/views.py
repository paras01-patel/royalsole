from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Report,Help,Userpordect,Merchant_signup
from django.core.mail import send_mail
from django.conf import settings


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

        if username=='admin123' and password=='admin':
            request.session['username']='admin123'
            request.session['password']='admin'
            messages.success(request,'admin login successfully')
            return redirect('adminpanel') 
        
        try:
            user = User.objects.get(username=username)

            if user.check_password(password):
                request.session["username"] = user.username
                request.session["email"] = user.email
                
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


def setting(req):
    return render(req,'setting.html')

def profile(req):
    return render(req,"setting.html",{"profile":True})



def security(req):
    return render(req,'setting.html',{'security':True})

def help(req):
    if req.method=="POST":
        username=req.POST.get('username')
        email=req.POST.get('email')
        topic=req.POST.get('topic')
        message=req.POST.get('message')
        
        
        d=Help.objects.create(
            username=username,
            email=email,
            topic=topic,
            message=message
        )
        d.save()
        return redirect('setting')        
    return render(req,'setting.html',{'help':True})

def report(req):
    if req.method=="POST":
        username=req.POST.get('username')
        email=req.POST.get('email')
        report_type=req.POST.get('report_type')
        des=req.POST.get('des')
        
        
        data=Report.objects.create(
            username=username,
            email=email,
            report_type=report_type,
            des=des
        )
        data.save()
        return redirect('setting')        
    return render(req,'setting.html',{'report':True})

def order(req):
    return render(req,'setting.html',{'order':True})




def djangoemail(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        contact = req.POST.get("contact")
        query = req.POST.get("query")

        send_mail(
            subject="Testing from Django",
            message=(
                f"Email from: {email}\n"
                f"Name: {name}\n"
                f"Contact: {contact}\n"
                f"Query: {query}"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["paraschandrawanshi649@gmail.com"],
            fail_silently=False,
        )

        return HttpResponse("MAIL DONE")

    return HttpResponse("Invalid Request")



def adminpanel(req):
    return render(req,"adminpanel.html")

def help_requests(req):
    data = Help.objects.all()

    return render(req, 'adminpanel.html', {
        'help_requests': True,
        'data': data,
    })
def issue_reports(req):
    data = Report.objects.all()

    return render(req, 'adminpanel.html', {
        'issue_reports': True,
        'data': data,
    })
    
    
def merchant(req):
    return render(req,'merchant.html')


def merchant_sign(req):
    if req.method == "POST":
        username = req.POST.get("username")
        email = req.POST.get("email")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")

        # Password Match Check
        if password != confirm_password:
            messages.error(req, "Password does not match")
            return redirect("merchant_sign")

        # Username Check
        if Merchant_signup.objects.filter(username=username).exists():
            messages.error(req, "Username already exists")
            return redirect("merchant_sign")

        # Email Check
        if Merchant_signup.objects.filter(email=email).exists():
            messages.error(req, "Email already exists")
            return redirect("merchant_sign")

        # Save Merchant
        Merchant_signup.objects.create(
            username=username,
            email=email,
            password=password
        )

        messages.success(req, "Merchant Signup Successfully")
        return redirect("merchant_login")

    return render(req, "merchant_sign.html")


def merchant_login(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        try:
            merchant = Merchant_signup.objects.get(email=email)

            if merchant.password == password:
                req.session["merchant_id"] = merchant.id
                req.session["merchant_username"] = merchant.username

                messages.success(req, "Login Successfully")
                return redirect("merchant")

            else:
                messages.error(req, "Invalid Password")
                return redirect("merchant_login")

        except Merchant_signup.DoesNotExist:
            messages.error(req, "Email does not exist")
            return redirect("merchant_login")

    return render(req, "merchant_login.html")