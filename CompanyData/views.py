from django.shortcuts import render
from django.views.generic import ListView

from django.http import HttpResponse
from .models import Basic
from .news_article import google_news_links

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
    links = google_news_links(s)
    return render(request,"show.html",{'s':s1, 'l':links})

def homepage(request):
    return render(request,"home.html")
    

