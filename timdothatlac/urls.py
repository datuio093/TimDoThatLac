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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , home.get_home,name="home"),
    path('accounts/login/' ,  home.get_login, name="login"),
    path('accounts/register/', home.get_register, name="register"),
    path('',home.get_home),
    path('timkiem/' , home.get_tim_kiem_post,  name="tim_kiem_post"),
    path('blog/' , home.get_blog,name="blog"),
    path('blog/<event_id>/' , home.get_blog_chi_tiet, name="blog_chi_tiet"), 

  
    path('dangtin/' , home.get_dang_tin,name="post"),

    path('editaccount/' , home.get_doi_mat_khau),

    #post
    path('mypost/' , home.get_my_post, name="mypost"),
    path('mypost/delete/<event_id>',home.delete_post, name="delete_post"),
    path('show/<event_id>', home.show_post, name="show_post"),
  


    path('chitiet/' , home.get_chi_tiet),
    path('logout/',home.logout_user,name="logout"),
    path('activate/<uidb64>/<token>' , home.get_activate, name="activate"),

    # #cmt
    # path('send-comment', home.send_comment, name="send_comment"),
    # path('comment/<event_id>', home.get_my_cmt, name="send_comment"),


    #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path('password_reset/done',auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

    #change password
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html"),name="change_password" ),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name="registration/change_password_done.html"), name="password_change_done")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

