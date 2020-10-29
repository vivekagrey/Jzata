from django.shortcuts import render
from django.views.generic import ListView
import pandas as pd
from django.http import HttpResponse
from .models import Basic

def create(request):
    
    s=Basic.objects.all().filter(name="ideaForge")
    print(s)
    return HttpResponse(s)



def search(request):
    s=request.POST.get('temp')
    s=s.strip()
    
    s1=Basic.objects.all().filter(name__contains=s)
   
    return render(request,"show.html",{'s':s1})

def king(request):
    return render(request,"home.html")
    

