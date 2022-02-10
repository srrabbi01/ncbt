from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.

@login_required(login_url='login')
def index_view(request):
    return render(request,'std_portal/index.html')

@login_required(login_url='login')
def financial_view(request):
    finansObjs = Financial.objects.filter(student = request.user.studentregistrationuni)
    context = {
        'finansobjs':finansObjs
    }
    return render(request,'std_portal/financial.html',context)

@login_required(login_url='login')
def result_view(request):
    resultObjs = Result.objects.filter(student = request.user.studentregistrationuni)
    context = {
        'resultobjs':resultObjs
    }
    return render(request,'std_portal/result.html',context)

@login_required(login_url='login')
def enroll_view(request):
    enrollObjs = Enroll.objects.filter(student = request.user.studentregistrationuni)
    context = {
        'enrollobjs':enrollObjs
    }
    return render(request,'std_portal/enroll.html',context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username =  request.POST.get('username')
            password =  request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request,"Username or Password didn't match. Please try again!")
    return render(request, 'std_portal/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')