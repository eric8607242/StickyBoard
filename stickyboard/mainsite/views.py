import json
import random

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from userauth.models import *
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    current_user = None
    if request.user.is_authenticated is True:
        current_user = request.user
    return render(request,"./mainsite/index.html",{'user':current_user})

def about(request):
    current_user = None
    if request.user.is_authenticated is True:
        current_user = request.user
    return render(request, "./mainsite/about.html", {'user':current_user})


@login_required(login_url='/account/login/')
def manageboard(request):
    user = request.user
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
        invite_user = User.objects.get(username=invite_username)
        
        if user.userboardid.get(board_name=board_name):
            board = UserBoardId.objects.get(board_name=board_name)
            invite_status = InviteStatus(board = board, inviter = user.username, user = invite_user, board_name = board_name)
            invite_status.save()
        return HttpResponse("invite_success")

def invitestatus(request):
    if request.method == "POST":
        user = get_user(request)
        invite_status = InviteStatus.objects.filter(user=user)
        
        status = []
        for i in invite_status:
            status_info = {
                "panel_name":i.board_name,
                "inviter":i.inviter
            }
            status.append(status_info)
        
        status_str = json.dumps(status)
        return HttpResponse(status_str)
    return HttpResponse("failed")

def deleteboard(request):
    if request.method == "POST":

        board_name = request.POST['board_name']
        user = get_user(request)

        board = UserBoardId.objects.get(board_name = board_name, user=user)
        if board is not False:
            board.delete()
            return HttpResponse("success")
        return HttpResponse("failed")

def refuserelation(request):
    if request.method == "POST":
        inviter_name = request.POST['inviter_name']
        board_name = request.POST['panel_name']
        user = get_user(request)
    
        invite_status = InviteStatus.objects.get(inviter=inviter_name, user=user, board_name=board_name)
        invite_status.delete()

        return HttpResponse("delete success")
    

def acceptrelation(request):
    if request.method == "POST":
        inviter_name = request.POST['inviter_name']
        inviter = User.objects.get(username = inviter_name)

        board_name = request.POST['panel_name']
        user = get_user(request)

        invite_status = InviteStatus.objects.get(inviter=inviter_name, user=user, board_name=board_name)
        invite_status.delete()

        board = UserBoardId.objects.get(user=inviter, board_name=board_name)
        board.user.add(user)
        user.userboardid.add(board)

        return HttpResponse("accept success")


def get_user(request):
    user_id = request.user
    user = User.objects.get(username = user_id)
    return user

