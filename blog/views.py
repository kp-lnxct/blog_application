from django.shortcuts import render, redirect
from django.contrib import messages
from urllib import request

from django.contrib.auth.forms import UserCreationForm #
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

post = {
    'author':'Name',
    'title': 'Blog Post',
    'content' : 'First Post Content',
    'data_posted' : 'December 30, 2021'
}



def home_page(request):
    return render(request,'blog/home.html')

def admin_form(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserCreationForm()

    return render(request, 'blog/register.html',{'form':form, 'type':'form'})

def admin_form_class(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserRegisterForm()

    return render(request, 'blog/register.html',{'form':form, 'type':'class'})

def admin_crispy_form(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserRegisterForm(request.POST)

        if form.is_valid():
    
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserRegisterForm()

    return render(request, 'blog/register.html',{'form':form, 'type':'crispy'})
    
# Admin Login Area

@login_required
def admin_profile(request):
    return render(request,'blog/profile.html')


def show_article(request):
    
    return render (request, 'blog/article.html')


 
