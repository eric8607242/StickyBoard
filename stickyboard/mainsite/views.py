from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from userauth.models import *
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

import random
# Create your views here.

def home(request):
    current_user = None
    if request.user.is_authenticated:
        current_user = request.user
    return render(request,"./mainsite/home.html",{'user':current_user})


@login_required(login_url='/account/login/')
def manageboard(request):
    user = get_user(request)
    return render(request,"./mainsite/usermanage.html",{"userboards":user.userboardid.all()})


@csrf_exempt
def createboard(request):
    boardname = request.POST['boardname']
    user = get_user(request)
    board = UserBoardId(board_name=boardname)
    board.save()
    board.user.add(user)

    user.userboardid.add(board)
    return HttpResponse("success")


def invite(request):
    user = get_user(request)
    
    board_id = request.POST['board_id']
    invite_username = request.POST['user_id']
    
    invite_user = User.objects.get(username=invite_username)
    
    if user.userboardid.get(id=board_id):
        board = UserBoardId.objects.get(id=board_id)
        invite_user.userboardid.add(board)
    return HttpResponse("invite_success")

def directboard(request):
    board_name = request.GET['board_name']
    user = get_user(request)
    html = render_to_string("./mainsite/panel.html", {"board_name":board_name, "user":user})
    # return render(request, "./mainsite/panel.html", {"board_name":board_name, "user":user})
    return HttpResponse(html)


def get_user(request):
    user_id = request.user
    user = User.objects.get(username = user_id)
    return user

