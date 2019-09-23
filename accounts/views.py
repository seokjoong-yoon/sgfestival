from django.shortcuts import render, redirect
from .forms import MyuserCreationForm
from .models import Myuser
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request, 'schedule/home.html')
def guide(request):
    return render(request, 'schedule/guide.html')
    
def register(request):
    if request.method == "POST":
        if request.POST['password1']!=request.POST['password2']:
            return render(request, 'schedule/register.html', {'context': '비밀번호가 일치하지 않습니다.'})
        else:
            username=request.POST['username']
            password=request.POST['password1']
            dpt=request.POST['dpt']
            Myuser.objects.create_user(username=username, password=password, dpt = dpt)
            newuser = auth.authenticate(username=username,password=password)
            auth.login(request, newuser)
            return redirect('home')
    elif request.method =="GET":
        return render(request, 'schedule/register.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'schedule/login.html', {'context': '등록되지 않은 회원입니다'})
    else:
        return render(request, 'schedule/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')