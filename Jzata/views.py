from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView 



def home(request):
    return render(request,'home.html')

def plans(request):
    return render(request,'plans.html')

def new(request):
    return render (request,"new.html")

def gdpr(request):
    return render (request ,"gdpr.html")

def privacy(request):
    return render (request,'privacy.html')

def service(request):
    return render (request,'service.html')

class Blog(ListView):
    model=Blog
    template_name="blog.html"

def resend_otp(request):
    if request.method == "GET":
        get_usr =request.GET['usr'] 
        if User.objects.filter(username = get_usr).exists() and not User.objects.get(username =get_usr).is_active:
            usr=User.objects.get(username=get_usr)
            mess=f"hello {usr.first_name},\n your otp is {usr_otp}\n Thanks!"  

            send_mail(
                "welcome to ITScorer - Verify your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )   

def paypal(request):
    return render(request,'payment.html')