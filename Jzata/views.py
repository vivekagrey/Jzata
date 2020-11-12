from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView 



def home(request):
    return render(request,'home.html')

def plane(request):
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
