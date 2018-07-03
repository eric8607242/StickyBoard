from django.urls import path, re_path

from . import views

app_name = 'board'

urlpatterns = [
    path(r'saveboard/', views.saveboard, name='saveboard'),
    path(r'loadboard/', views.loadboard, name='loadboard'),
    re_path(r'^directboard/(?P<board_name>\w+)/(?P<board_id>\d+)/$',views.directboard,name='directboard'),
]

