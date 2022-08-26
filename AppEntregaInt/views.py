from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime

# Create your views here.

def inicio(request):
    return HttpResponse('vista inicio')

def equipo(request):
    return HttpResponse('vista equipo')    

def unittest(request):
    return HttpResponse('vista unittest')       

def regressiontest(request):
    return HttpResponse('vista regressiontest')     