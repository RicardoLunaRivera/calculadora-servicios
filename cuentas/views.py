from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def vista_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html',{'form':form})

def vista_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
