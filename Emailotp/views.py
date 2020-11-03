from django.shortcuts import render ,redirect
from .forms import Signupform
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .models import UserOTP
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import logout
def signup(request):

    if request.method=='POST':
        print("welcome ")
        get_otp=request.POST.get('otp')

        if get_otp:
            get_usr =request.POST.get('usr')
            print("anjali")
            usr=User.objects.get(username=get_usr)
            print("mia")
            if not usr.is_active:
                print("halifa")
                if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                    usr.is_active=True
                    usr.save()
                    messages.success(request,f'Account is created for {usr}')
                    return redirect("login")
                else:
                    messages.error(request,f'Enter wrong otp')
                    return render(request,'signup.html',{'otp':True ,'usr':usr})
        form =Signupform(request.POST)
        if form.is_valid():
            print("im here") 
            form.save()
            username =form.cleaned_data.get('username')
            name=form.cleaned_data.get('name').split(' ')

            usr=User.objects.get(username=username)
            usr.email=username
            usr.first_name=name[0]
            try:
                usr.last_name=name[1]
            except:
                usr.last_name=""
            usr.is_active=False
            usr.save() 
            usr_otp=random.randint(1000,9999)
            UserOTP.objects.create(user=usr,otp=usr_otp)
            mess=f"hello {usr.first_name},\n your otp is {usr_otp}\n Thanks!"  

            send_mail(
                "welcome to ITScorer - Verify your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )             
            messages.success(request,f'Account is Created For {username}')
            return render(request,'signup.html',{'otp':True,'usr':usr})
    else:
        form=Signupform()
    print("welcome 2")
    return render(request,'signup.html',{'form':form})   

def login(request):

    if request.method=="POST":
        username=request.POST['t1']
        password=request.POST['t2']
        username=username.strip()
        password=password.strip()
        print(password)
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("welcome to this page")
            return render(request,'home.html')         
        else:
            print("not found")
            return render(request,'home.html')  
    return render(request,'login.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'home.html')