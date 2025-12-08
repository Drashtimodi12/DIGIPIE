from django.shortcuts import render, render, HttpResponse
# from DMart_Application.models import *

# Create your views here.

def welcome_page(request):
    return render(request, 'Welcome_Page.html')