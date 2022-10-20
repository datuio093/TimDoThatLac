from django.shortcuts import render

# Create your views here.

def get_home(request):
    return render(request, 'home.html')

def get_login(request):
    return render(request, 'login.html')

def get_register(request):
    return render(request, 'register.html')

def get_search(request):
    return render(request, 'timkiem.html')

def get_blog(request):
    return render(request, 'blog.html')

def get_blog_meo_hay(request):
    return render(request, 'blogmeohay.html')