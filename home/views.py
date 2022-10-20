from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def get_home(request):
    return render(request, 'home.html')

def get_login(request):
    return render(request, 'login.html')

def get_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful." )
        return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form":form})

def get_search(request):
    return render(request, 'timkiem.html')

def get_blog(request):
    return render(request, 'blog.html')

def get_blog_meo_hay(request):
    return render(request, 'blogmeohay.html')