from base64 import urlsafe_b64decode
# from email.message import EmailMessage
from gzip import FNAME
from lib2to3.pgen2.tokenize import generate_tokens
from multiprocessing import context
from tkinter.messagebox import NO
from unittest.result import failfast
from timdothatlac import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_tokens
# from .form import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages
# Create your views here.


def get_home(request):

    return render(request, 'home.html' , )

def get_login(request):
    
    if request.method == "POST":
         username = request.POST['user']
         pass1 = request.POST['pass']

         users = authenticate(username=username, password = pass1)

        #  if users.is_active == False:
        #     messages.error(request, "You Must Be Confirm Email Before Login")
        #     return redirect('login')
        

         if users is not None:
            login(request,users)
            # return redirect('home')
            fname = users.first_name
            lname = users.last_name
            return render( request , 'home.html' , {'fname' : fname, 'lname' : lname}  )
            # return redirect('login', {'fname' : fname, 'lname' : lname})
         else:
            messages.error(request, "Login Fail")           
            
    return render(request , 'login.html')

def get_register(request):
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
 