from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib import auth
from  django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

import os
import cv2
from .models import *

# Create views here.
def index(request):
    return render(request,'index.html')

def verifyRequest(request):
    try:
        a=1
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
    
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username,password=password)
           
            print(user.is_authenticated, "fdigjd")
           
            print(user)
            if user is not None:
                match = facerecognize(user.get_username())
                print(match)
                try:
                    if (match):
                        auth.login(request,user)
                        return render(request,'indexes.html')
                    else:
                        messages.info(request,'Face couldn\'t Recognized')
                        return redirect('login')
                  
                except:
                    # Handle authentication failure
                    
                    messages.info(request,'Face couldn\'t recognized')
                    return redirect('login')
                       
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    except:
        messages.info(request,'Examee not appeared')
        return render(request,'login.html')

def home(request):

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user taken')  
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
        
            else:
                image = faceCaptureSave(username)
                image = str(image)
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()  
                return redirect('login')
        else:
            messages.info(request,'Passwords Not Matching...')
            return redirect('register')
    
def login(request):
    return render(request,'login.html')

def logout(request):
    return redirect(request,'index.html')

def about(request):
    return render(request,'about_us.html')

def contact(request):
    return render(request,'contact.html')

def indexes(request):
    return render(request,'indexes.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def register(request):
    return render(request,'register.html')

def verify(request):
    return render(request,'verify.html')


def cques(request):
    return render(request,'c_questions.html')

def cstart(request):
    
    return render(request,'c_start.html')

def questions(request):
    return render(request,'python_questions.html')

def quizStart(request):
    
    return render(request,'python_start.html')

def java(request):
    return render(request,'java_start.html')

def javaques(request):
    return render(request,'java_questions.html')

def javascript(request):
    return render(request,'javascript_start.html')

def javascriptques(request):
    return render(request,'javascript_questions.html')

def cpp(request):
    return render(request,'cpp_start.html')

def cppques(request):
    return render(request,'cpp_questions.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



