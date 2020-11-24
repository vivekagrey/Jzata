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

        s=request.POST.get('t1')
        s2=request.POST.get('t2')
        s=s.strip()
        s2=s.strip()
    

        user=authenticate(username=s,password=s2)
        login(request,user)
        if user is not None:
            login(request,user)
            return render(request,"home.html")
        else:
            return HttpResponse("not a user")
    return render(request,"login.html")
    

def check(request):
    s=request.POST.get('temp')
    print(s)
    s=s.strip() 
    s1=Basic.objects.all().filter(name=s)
    list1=[]
    for i in s1:
        cin=i.cin

        Investor =i.Investor

        Products=i.Products

        name=i.name

        Website=i.website
       
        Industry=i.Industry
        
        Headquatars=i.Headquatars
       
        Type=i.type
     
        Founded=i.founded
        
        Specialities=i.specialities
        
        Linkedin=i.linkedin
          
        Domain=i.domain
        
        Logo=i.logo
        
        Description=i.description
        
        Companyno=i.company_no
        
        incorporation_date=i.incorporation_date
        
        register_address=i.register_address
        
        Industry_code=i.Industry_code
        
        Company_Registered_Name=i.Company_Registered_Name
        
        roc=i.Roc
            
        director_detail=i.director_detail 

        description=i.description                   
                    

    cart={}
    cart['description']=description     
    cart['cin']=cin
    
    cart['website']=Website

    cart['Industry'] =Industry
  
    cart['Headquatars']=Headquatars
 
    cart['Type']=Type
    cart['Founded']=Founded   
    cart['Specialities']=Specialities    
    cart['Linkedin']=Linkedin  
   
    cart['Domain']=Domain  
    cart['Logo']=Logo  
    cart['Description']=Description   
        
    cart['companyno']=Companyno 
    
    cart['incorporation_date']=incorporation_date 
    cart['register_address']=register_address  
    cart['Industry_code']=Industry_code 
   
    cart['Company_Registered_Name']=Company_Registered_Name   
    cart['roc']=roc        
    

    ld=director_detail.split(',')  
    cart['ld']=ld

    l1=Products.split(',')    
    cart['l1']=l1
    l2=Investor.split(',') 
    cart['l2']=l2

        

    return render(request,"final_profile.html",cart)


def canvas(request):
    return render(request,"canvas.html")