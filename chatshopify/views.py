from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import AddField
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
            return HttpResponse("Your Password and Confirm Password are not same")
        else:
            my_user=User.objects.create_user(first_name=fname,last_name=lname ,username=username,email=email,password=pass1)
            my_user.save()
            return redirect('Login')
            print(uname,email,pass1,pass2)

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
            return HttpResponse("Email or Password is incorrect")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('Login')

def userprofile(request):
    current_user = request.user
    context = {
        'data': current_user
    }
    return render (request,'user-profile.html',context)

# views.py

def savechanges(request):
    current_user = request.user

    if request.method == 'POST':
        current_user.fname = request.POST.get('Fname')
        current_user.lname = request.POST.get('Lname')
        
       
        current_user.username =request.POST.get('username')
        current_user.email = request.POST.get('email')
        current_user.save()
        
        country = request.POST.get('country')
        obj = AddField(user_id=current_user, country=country)
        obj.save()
    return HttpResponse("updated")

    

        
    
    
    
