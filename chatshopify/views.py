from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import AddField
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import UploadFile

import os
from django.conf import settings
def welcome(request):
     return render(request,'welcome.html')

def index(request):
    current_user = request.user
    context = {
        'data': current_user
    }
    return render (request,'index.html',context)

def Signup(request):
    if request.method=='POST':
        fname=request.POST.get('Fname')
        lname=request.POST.get('Lname')
        username = f"{fname}{lname}"
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        country=request.POST.get('country')
        
        if pass1!=pass2:
            messages.success(request, "Your Password and Confirm Password are not same")
            return redirect(request.META['HTTP_REFERER']) 
        else:
            my_user = User.objects.create_user(first_name=fname,last_name=lname ,username=username,email=email,password=pass1)
            my_user.save()
            
            obj = AddField(user_id = my_user, country = country)
            obj.save()
            
            return redirect('Login')


    return render (request,'signup.html')
     

def Login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        pass1=request.POST.get('password1')

        user=authenticate(request,username = email,password = pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
           messages.success(request, "User name or password is incorrect")
           return redirect(request.META['HTTP_REFERER'])

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('Login')

def userprofile(request):
    current_user = request.user
    country = AddField.objects.get(user_id = current_user.id)
    print(f"{str(country)}")
    context = {
        'data': current_user,
        'country' :country
    }
    return render (request,'user-profile.html',context)

# views.py

def savechanges(request):
    current_user = request.user

    if request.method == 'POST':
        current_user.fname = request.POST.get('Fname')
        current_user.lname = request.POST.get('Lname')
        #current_user.username =request.POST.get('username')
        current_user.email = request.POST.get('email')
        current_user.pass1 = request.POST.get('pass1')
        current_user.save()
        
        country = request.POST.get('country')
        
        
        obj = AddField.objects.get(user_id=current_user)
        obj.country = country
        obj.save()
        
        
        messages.success(request, "Profile details updated!")
    return redirect(request.META['HTTP_REFERER'])
    
    
def upload_dataset (request):
    current_user = request.user
    country = AddField.objects.get(user_id = current_user.id)
    
    context = {
        'data': current_user,
        'country' :country
    }
    return render (request,'upload-dataset.html',context)


def save_file(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        file = request.FILES['uploadedfile']
        obj = UploadFile(title=title, document = file)
        obj.save()
        messages.success(request, "file uploaded!")
    return redirect(request.META['HTTP_REFERER'])
        
def app_chat_box(request):
    current_user = request.user
    country = AddField.objects.get(user_id = current_user.id)
    
    context = {
        'data': current_user,
        'country' :country
    }
    return render(request,'app-chat-box.html',context)    

from .QAmodel import callQuestion

def question_answering(request):
    question = ""
    if request.method == 'POST':
        question=request.POST.get('question')
        question=callQuestion(question)
        print(question)
    return render(request, 'app-chat-box.html', {'question': question})
    

