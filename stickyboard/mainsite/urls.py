from django.urls import path,re_path,include
from . import views

app_name = 'mainsite'

urlpatterns = [
    path(r'home/',views.home,name='home'),
    path(r'manageboard/',views.manageboard,name='manageboard'),
    path(r'mainsite/createboard/',views.createboard,name='createboard'),
    path(r'invite/',views.invite,name='invite'),
    re_path(r'^mainsite/directboard/$',views.directboard,name='directboard'),
]
