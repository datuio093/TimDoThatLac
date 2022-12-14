from base64 import urlsafe_b64decode
from email import message
# from email.message import EmailMessage
from gzip import FNAME
from lib2to3.pgen2.tokenize import generate_tokens
from multiprocessing import context
import re
from tkinter.messagebox import NO
from turtle import title
from unittest.result import failfast
from timdothatlac import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_tokens
from .models import mypost,comment
from .form import *
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .form import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages
# Create your views here.


def get_home(request):
    
    if request.method == "GET":
        data = mypost.objects.filter(type="Đồ Thất Lạc").order_by('id')[:3]
        context = {
            'mypost':data
        }
        data1 = mypost.objects.filter(type="Đồ Nhặt Được").order_by('id')[:3]
        context = {
            'mypost1':data1
        }
        return render(request, "home.html" , {'mypost':data, 'mypost1':data1})
    
    return render(request, 'home.html' )

def get_login(request):

    #redirect to home when user signin
    if request.user.is_authenticated:
        return redirect('home')   
    
    if request.method == "POST":
         username = request.POST['user']
         pass1 = request.POST['pass']

         users = authenticate(username=username, password = pass1)

        #  if users.is_active == False:
        #     messages.error(request, "You Must Be Confirm Email Before Login")
        #     return redirect('login')
 

         if users is not None:
            login(request,users)
            
            fname = users.first_name
            lname = users.last_name
            return render( request , 'welcome.html' , {'fname' : fname, 'lname' : lname}  )
            
         else:
            messages.error(request, "Login Fail")   
            
          
            
    return render(request , 'login.html')

def get_register(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == "POST":

        email = request.POST['Email']
        username = request.POST['User']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['Password1']
        pass2 = request.POST['Password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exist")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Password didn't match")
            return redirect('register')

        if not username.isalnum():
             messages.error(request, "Username must be Alpha-Numberic !")
             return redirect('register')

       
        myuser = User.objects.create_user(username , email , pass1 )
        myuser.first_name = fname
        myuser.last_name = lname
    
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been successfully created")

        # Welcome email

        subject = "Welcome to Django"
        message = "Hello " + myuser.first_name + myuser.last_name
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject , message ,from_email , to_list, fail_silently=True)

        # Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email Django"
        message2 = render_to_string('email_confirmation.html',{
            'fname' : myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_tokens.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],

        )
        email.fail_silently = True
        email.send()


        return redirect('login')
    return render(request, 'register.html')


def get_search(request):
    return render(request, 'timkiem.html')

def get_blog(request):
 
    if request.method == "GET":
        data = blog.objects.filter().order_by('-pk')
        context = {
            'blog':data
        }
        return render(request, "blog.html" , {'blog':data})
    return render(request, 'blog.html')

def get_blog_chi_tiet(request,event_id):
    event = blog.objects.get(pk=event_id)
    return render(request, 'blogmeohay.html', {'event':event})

def get_dang_tin(request):
    if request.user.is_authenticated == False:
        return redirect('login') 
    # create post 
    if request.method == "POST":
        username = request.POST['username']
        title = request.POST['tieude']
        type = request.POST['luachon']
        object = request.POST['loai']
        descrip = request.POST['mota']
        v1,address = request.POST['country'].split('-')
        v1,city = request.POST['city'].split('-')
        v1,district =  request.POST['district'].split('-')
        name = request.POST['name']
        pnum = request.POST['pnum']
        email = request.POST['email']
        images = request.FILES.get('images')
    #save post to db
        Mypost = mypost.objects.create(user=username,title=title, type=type,object=object,descrip=descrip,address=address,city=city,district=district,name=name,pnum=pnum,email=email,images=images)
        # ,city=city,district=district
        Mypost.save()
    #display successfull post messages
        messages.success(request, "Your Post has been successfully create")
    #redirect to main page or mypost
        return redirect('mypost')
    return render(request, 'dangtin.html')

def get_chi_tiet(request):
    return render(request, 'chitiet.html')

def get_doi_mat_khau(request):
    return render(request, 'doimatkhau.html')


def get_my_post(request):
    #get data sorted by ID
    if request.method == "GET":
        onedata = mypost.objects.filter().order_by('-pk')
        page = request.GET.get('page', 1)
        context = {
            'post':onedata
        }
        paging = Paginator(onedata, per_page=6)
        try:
            post = paging.page(page)
        except PageNotAnInteger:
            post = paging.page(1)
        except EmptyPage:
            post = paging.page(paging.num_pages)

    #render data to html

    return render(request, 'mypost.html', {'post':post})

def get_tim_kiem_post(request):

    if request.method == "POST":
        onedata = mypost.objects.filter(type=request.POST['type']).filter(object=request.POST['loai']).order_by('-pk')
        page = request.GET.get('page', 1)
        context = {
            'post':onedata
        }
        paging = Paginator(onedata, per_page=12)
        try:
            post = paging.page(page)
        except PageNotAnInteger:
            post = paging.page(1)
        except EmptyPage:
            post = paging.page(paging.num_pages)

    #render data to html
        return render(request, 'timkiem.html', {'post':post})
    return render(request, 'timkiem.html')


def get_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError , User.DoesNotExist ):
        myuser : None

    if myuser is not None and generate_tokens.check_token(myuser , token):
        myuser.is_active = True
        myuser.save()
        login(request , myuser) 
        return redirect('home')
    else:
        return redirect(request, 'activation_fail.html')
 
def logout_user(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('login')

def delete_post(request, event_id):
    event = mypost.objects.get(pk=event_id)
    event.delete()
    return redirect('mypost')


def show_post(request, event_id):
    event = mypost.objects.get(pk=event_id)

    if request.method == "GET":
        data = comment.objects.filter().order_by('-pk')
        context = {
            'cmt':data
        }
        return render(request, "chitiet.html" , {'event': event,  'cmt':data})

        
    if request.method == "POST":
        if request.user.is_authenticated == False:
            return redirect('login') 
        user = request.user.username 
        postid = event_id
        email = request.POST['email']
        message = request.POST['message']
    #save post to db
        # if(request.POST.checked('check_hide') != True):
        Cmt = comment.objects.create(user=user,postid=postid,mail=email,message=message)
        Cmt.save()
        # else:
        #     Cmt = comment.objects.create(user="Ẩn Danh",postid=postid,mail="Ẩn Danh",message=message)
        #     Cmt.save()
        data = comment.objects.filter().order_by('-pk')
        context = {
            'cmt':data
        }
        return render(request, "chitiet.html" , {'event': event,  'cmt':data})
        
    return render(request, 'chitiet.html'  , {'event': event} )

def show_profile(request):
    if request.method == "POST":
        username = request.user.username 
        user = User.objects.get(username = username)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return render(request, 'profile.html')
    return render(request, 'profile.html')


