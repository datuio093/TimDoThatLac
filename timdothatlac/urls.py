"""timdothatlac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function viewsss
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , home.get_home,name="home"),
    path('login/' ,  home.get_login),
    path('register/', home.get_register),
    path('',home.get_home),
    path('timkiem/' , home.get_search),
    path('blog/' , home.get_blog),
    path('blog/meohay/' , home.get_blog_meo_hay),
    path('dangtin/' , home.get_dang_tin),
    path('editaccount/' , home.get_doi_mat_khau),
    path('mypost/' , home.get_my_post),
      path('chitiet/' , home.get_chi_tiet)


]
