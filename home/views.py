from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# from .form import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages
# Create your views here.


def get_home(request):
    return render(request, 'home.html')

def get_login(request):
    
    if request.method == "POST":
         username = request.POST['user']
         pass1 = request.POST['pass']

         users = authenticate(username=username, password = pass1)

         if users is not None:
            login(request,users)
            return redirect('home')
         else:
            messages.error(request, "Fail")           
            
    return render(request , 'login.html')

def get_register(request):
    if request.method == "POST":

        email = request.POST['Email']
        username = request.POST['User']
        pass1 = request.POST['Password1']
        pass2 = request.POST['Password2']
       
        myuser = User.objects.create_user(username , email , pass1 )
        myuser.save()
        messages.success(request, "Your Account has been successfully created")
        return redirect('login')
    return render(request, 'register.html')


def get_search(request):
    return render(request, 'timkiem.html')

def get_blog(request):
    return render(request, 'blog.html')

def get_blog_meo_hay(request):
    return render(request, 'blogmeohay.html')

def get_dang_tin(request):
    return render(request, 'dangtin.html')

def get_chi_tiet(request):
    return render(request, 'chitiet.html')

def get_doi_mat_khau(request):
    return render(request, 'doimatkhau.html')


def get_my_post(request):
    return render(request, 'mypost.html')