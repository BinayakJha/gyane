from django import template
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
# email
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
import math, random

from .models import UserOTP

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.

# ------------------------------------------------------------------------------------
# home function
# ------------------------------------------------------------------------------------

def home(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/register.html')

def verify(request):
   return render(request, 'core/token_verify.html')
        
def forgot_password(request):
    return render(request, 'core/forgot-password.html')

def home_logged(request):
    return render(request, 'core/home.html')
# signup function

def handleSignUp(request):  # sourcery no-metrics
    if request.method == "POST":
        # Get the post parameters
        get_otp = request.POST.get('otp')
        
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.is_staff = True
                usr.save()
                messages.success(request, "Account Activated")
                template1 = get_template('core/welcome_email.html').render({'name': usr.username})
                subject = 'Thankyou For Joining Gyan-e Team.'
                email = EmailMessage(
                    subject,
                    template1,
                    settings.EMAIL_HOST_USER,
                    [usr.email, ],

                )
                email.fail_silently = False
                email.content_subtype = "html"
                email.send()
                return redirect("home")

            else:
                messages.error(request, "Invalid OTP")
                return render(request, 'core/register.html',{'otp':True, 'usr':usr})
        usernames = request.POST['username']
        email = request.POST['email']
        fname = request.POST['first_name']
        # # lname=request.POST['lname']
        pass1 = request.POST['password']
        pass2 = request.POST['password_repeat']
       
        

        # check if user/email already exsist or not

        if User.objects.filter(username=usernames).exists() and User.objects.filter(email=email).exists():
            messages.error(request, "Email and username already exsist.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, " Email already exsist.")
            return redirect('signup')

        if User.objects.filter(username=usernames).exists():
            messages.error(request, " Username already exsist.")
            return redirect('signup')

        # check for errorneous input

        if len(usernames) < 3:
            messages.error(
                request, " Your username must be under 10 characters")
            return redirect('signup')

        if not usernames.isalnum():
            messages.error(
                request, " Username should only contain letters and numbers")
            return redirect('signup')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        emails = authenticate(email=email)
        if emails is not None:
            messages.error(
                request, "Email you entered already exists. Please login or use different email")
            return redirect("signup")
        is_staff = True
        # Create the user
        myuser = User.objects.create_user(usernames, email, pass1)
        myuser.first_name = fname
        myuser.is_staff = False
        myuser.is_active = False
        myuser.save()
        myuser_otp = random.randint(100000, 999999)
        UserOTP.objects.create(user=myuser, otp=myuser_otp)
        template2 = get_template('core/token.html').render({ 'myuser_otp':myuser_otp})
        email_otp = EmailMessage (
            'Your OTP',
            template2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email_otp.fail_silently = False
        email_otp.content_subtype = "html"
        email_otp.send()
        return render(request, 'core/register.html', {'otp': True, 'usr':myuser})
        # messages.success(
        #     request, " Your account has been successfully created")
       
    #     # email
       
       
    else:
        return HttpResponse("404 - Not found")

    return redirect('home')

# def verify_check(request):
#     if request.method == "POST":
#         # Get the post parameters
#         token = request.POST['token']
#         letter  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         number  = '0123456789'
#         # make the random word of 4 characters
#         word = ''.join(random.choice(letter+number) for _ in range(6))
#         # token_template = get_template('core/token.html').render({'word':token_create()})
#         # token_email = EmailMessage(
#         #     'Verify your email',
#         #     token_template,
#         #     settings.EMAIL_HOST_USER,
#         #     [email],
#         # )
#         # token_email.content_subtype = "html"
#         # token_email.send()
#         if token == word:
#             print(User.objects.filter(email=request.user.email).filter(is_active=False)[0])

#             messages.success(request, "Your email has been verified")
#             print('SUCCESSSSSSSS')
#         else:
#             print(User.objects.filter(email=request.user.email).filter(is_active=False))
#             print('NOOOOOOOOOOOOO')
#         return redirect('home')

# login function
def handleLogin(request): 
    if request.method=="POST":
        # Get the post parameters
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginemail, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
        
    else:
        return HttpResponse("404- Not found")

# logout function
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

# password change 
def password_success(request):
    # return render (request,'registration/password_success.html')
    messages.success(request, "Password has been succesfully changed.")
    return redirect("home")

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'core/password_change.html'
    success_url = reverse_lazy('password_success')