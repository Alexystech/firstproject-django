from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def calculadora(request):

    return render(request, "PrimeraVista.html")

def video(request):
    return render(request,'video.html')