from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout 
from django.contrib import messages

def log_in(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request, "Böyle bir kullanıcı yok veya parola hatalı")
            return render(request,"user/login.html",context=context)
        messages.success(request,"Başarı ile giriş yaptınız")
        login(request,user)
        return render(request,"article/index.html")
    return render(request,"user/login.html",context=context)


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, 'Kullanıcı başarı ile kayıt edildi.')
        return redirect("art:index")
    else:
        if request.POST:
            messages.info(request, 'Kullanıcı kayıt edilemedi.')
    
    context = {
                "form" : form
                }
    return render(request,"user/register.html",context=context)
#Second way   
"""
    if request.method == "POST":
        form= RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login_in(request,newUser)
            
            return render(request,"user/login.html")
        else:
            context = {"form" : form}
            return render(request,"user/register.html",context=context)
    else:
        form=RegisterForm()
        context = {
            "form" : form
            }
        return render(request,"user/register.html",context=context)
"""


def log_out(request):
    logout(request)
    messages.success(request,"Sistemden çıkış yaptınız")
    return render(request,"article/index.html")
