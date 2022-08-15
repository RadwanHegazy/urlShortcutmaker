from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib import messages
from . import models

MAIN_URL = 'https://127.0.0.1:8000/'


def open (request,hash) :
    try:
        getLink = models.Link.objects.get(hash_code=hash)
        getLink.visitors = int(getLink.visitors) + 1
        getLink.save()
        return redirect(getLink.link)
    except models.Link.DoesNotExist:
        return HttpResponse('<h1>404 not found !</h1>')


def home (request) :


    if request.user.is_authenticated:

        if request.method == 'POST' :
            url = request.POST['url']
            models.Link.create_link(user=request.user,link=url)

        return render(request,'home.html')
    else :
        return redirect('signup')


def signup (request) :
    if request.method == "POST" :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        c = forms.CreateUser(username=username,email=email,password1=password1,password2=password2)
        if c['create']:
            getUser = User.objects.get(username=c['username'])
            auth_login(request,getUser)
            return redirect('home')
        else :
            messages.warning(request,c['errors'])
    return render(request,'signup.html')

def login (request) :
    if request.method == "POST" :
        email = request.POST['email']
        password = request.POST['password']
        log = forms.LoginForm(email=email,password=password)
        if log['login'] == False:
            messages.warning(request,log['error'])
        else :
            u = log['user']
            auth_login(request,u)
            return redirect('home')
    return render(request,'login.html')