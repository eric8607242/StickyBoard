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
    print(request.user.is_authenticated)
    if request.user.is_authenticated is True:
        current_user = request.user
        return render(request,"./mainsite/index.html",{'user':current_user})
    return render(request,"./mainsite/index.html",{"user":None})

def about(request):
    return render(request, "./mainsite/about.html")


@login_required(login_url='/account/login/')
def manageboard(request):
    user = request.user
    for t in user.userboardid.all():
        print(t)
    return render(request,"./mainsite/usermanage.html",{"user":user,"userboards":user.userboardid.all()})


@csrf_exempt
def createboard(request):
    boardname = request.POST['boardname']
    user = get_user(request)
    board = UserBoardId(board_name=boardname)
    board.save()
    board.user.add(user)

    user.userboardid.add(board)
    return HttpResponse("success")

@csrf_exempt
def invite(request):
    if request.method == "POST":
        user = get_user(request)
        
        board_name = request.POST['board_name']
        invite_username = request.POST['invitee']
        print(invite_username)
        invite_user = User.objects.get(username=invite_username)
        
        if user.userboardid.get(board_name=board_name):
            board = UserBoardId.objects.get(board_name=board_name)
            board.user.add(invite_user)
            invite_user.userboardid.add(board)
        return HttpResponse("invite_success")

def invitestatus(request):
    return HttpResponse("111")


def deleteboard(request, **kwargs):
    
    if request.method == "POST":
        board_name = request.POST['board_name']
        board_id = request.POST['board_id']
        user = get_user(request)

        board = UserBoardId.objects.get(id = board_id, user=user)
        if board is not False:
            board.delete()
            return HttpResponse("success")
        return HttpResponse("failed")

def get_user(request):
    user_id = request.user
    user = User.objects.get(username = user_id)
    return user

