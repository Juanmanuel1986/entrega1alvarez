from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime

# Create your views here.

def inicio(request):
    #return HttpResponse('vista inicio')
    return render(request, "AppEntregaInt/inicio.html")

def equipo(request):
    #return HttpResponse('vista equipo')    
    return render(request, "AppEntregaInt/equipo.html")

def unittest(request):
    #return HttpResponse('vista unittest')  
    return render(request, "AppEntregaInt/unittest.html")    

def regressiontest(request):
    #return HttpResponse('vista regressiontest')  
    return render(request, "AppEntregaInt/regressiontest.html") 