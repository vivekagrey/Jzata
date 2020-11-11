from django.shortcuts import render,redirect
from django.views.generic import ListView

from django.http import HttpResponse
from .models import Basic
from .news_article import google_news_links, news_extraction

from .form import Login
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required

def create(request):
    
    s=Basic.objects.all().filter(name="ideaForge")
    print(s)
    return HttpResponse(s)


def Build_Database(request):
    pass

def search(request):
    s=request.POST.get('temp')
    s=s.strip() 
    s1=Basic.objects.all().filter(name__contains=s)
    pos_news, neg_news = news_extraction(s)

    return render(request,"show.html",{'s':s1, 'pos_news':pos_news,'neg_news':neg_news})

def homepage(request):
    return render(request,"home.html")

def page(request):
    return render(request,'pricing.html')
    

def signup(request):
   pass


def login(request):
    if request.method=="POST":
        print("imhere")
        s=request.POST.get('t1')
        s2=request.POST.get('t2')
        s=s.strip()
        s2=s.strip()
    

        user=authenticate(username=s , password=s2)
        login(request,user)
        if user is not None:
            login(request,user)
            return render(request,"home.html")
        else:
            return HttpResponse("not a user")
    return render(request,"login.html")
    

def plans(request):
    return render(request,"plans.html")
