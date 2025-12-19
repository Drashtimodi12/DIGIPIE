from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from crudapp.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_data(request):
    if request.method=='POST':
        data = request.POST
        print(data)
    pass