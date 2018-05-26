from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'userauth'

urlpatterns = [
    #If called via GET, it displays a login form that POSTs to the same URL
    #If called via POST with user submitted credentials, it tries to log the user in
    path(r'login/',auth_views.LoginView.as_view(template_name = 'userauth/login.html'),name = 'login'),
    path(r'logout/',auth_views.LogoutView.as_view(template_name = 'userauth/logout.html'),name = 'logout'),
    path(r'signup/',views.signup,name="signup"),
]