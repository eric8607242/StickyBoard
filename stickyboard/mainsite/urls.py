from django.urls import path,re_path,include
from . import views

app_name = 'mainsite'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'about/', views.about, name='about'),
    path(r'manageboard/', views.manageboard, name='manageboard'),
    path(r'createboard/', views.createboard, name='createboard'),
    path(r'invite/', views.invite, name='invite'),
    path(r'invitestatus/', views.invitestatus, name='invitestatus'),
    path(r'deleteboard/', views.deleteboard, name='deleteboard')
]
