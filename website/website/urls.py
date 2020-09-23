from django.contrib import admin
from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('user_home',User_home,name="user_home"),
    path('admin_home/',Admin_Home,name="admin_home"),
    path('service_home',Service_home,name="service_home"),
    path('service',All_Service,name="service"),
    path('profile',profile,name="profile"),
    path('service_profile',service_profile,name="service_profile"),
    path('admin_profile',admin_profile,name="admin_profile"),
    path('contact',contact,name="contact"),
    path('login',Login_User,name="login"),
    path('admin_login',Login_admin,name="admin_login"),
    path('logout',Logout,name="logout"),
    path('signup',Signup_User,name="signup"),
    path('new_service_man',New_Service_man,name="new_service_man"),
    path('view_service',View_Service,name="view_service"),
    path('search_services',search_services,name="search_services"),
    path('explore_services(<int:pid>)',Explore_Service,name="explore_services"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
