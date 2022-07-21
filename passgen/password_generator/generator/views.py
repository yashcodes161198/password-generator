from django.shortcuts import render
from django.http import HttpResponse
import random
# def about(request):
    # the render function automatically looks inside a folder named "templates" in the 
    # same directory where views is present
    # you can change the name of the folder from templates to "manoj"
    # to do tha, you will have to go to settings.py -> TEMPLATES -> DIRS -> 
    # now enter the address of folder ie 'DIRS': ['generator/manoj'],
    # return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    charecters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        charecters.extend (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        charecters.extend (list('0123456789'))
    if request.GET.get('special'):
        charecters.extend (list('!@#$%^&*()_+|/*-+'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(charecters)
    
    return render(request, 'generator/password.html', {'password' : thepassword})






















