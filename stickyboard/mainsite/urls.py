from django.urls import path,include
from . import views

app_name = 'mainsite'

urlpatterns = [
    path(r'home/',views.home,name='home'),
    path(r'manageboard/',views.manageboard,name='manageboard'),
    path(r'createboard/',views.createboard,name='createboard'),
    path(r'invite/',views.invite,name='invite'),
]
