import json

from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from userauth.models import *
from django.contrib.auth.models import User

@csrf_exempt
def saveboard(request):
    if request.method == 'POST':
        board_name = request.POST['board_name']
        board_info = request.POST['board_info']
        board_info = json.loads(board_info)

        user = get_user(request)
        board = UserBoardId.objects.get(board_name = board_name, user = user)
        board_id = board.id
        
        for note_info in board_info:
            if checknote(note_info):
                new_note = Note(
                    title = note_info['title'],
                    comment = note_info['comment'],
                    color = note_info['color'],
                    background_color = note_info['background_color'],
                    note_id = note_info['board_id'],#################
                    board = board,
                )
                new_note.save()
            else:
                edit_note = Note.objects.get(note_id = note_info["board_id"])
                edit_note.title = note_info['title']
                edit_note.comment = note_info['comment']
                edit_note.color = note_info['color']
                edit_note.background_color = note_info['background_color']
                edit_note.save()
        
        db_note_count = Note.objects.filter(board = board).count()
        
        if db_note_count > len(board_info):
            for i in range(len(board_info), db_note_count):
                note = Note.objects.get(note_id = i+1, board = board)
                note.delete()
        return HttpResponse("success")

def checknote(note_info):
    note = Note.objects.filter(note_id = note_info["board_id"])
    if note.count() ==  0:
        return True
    return False

def directboard(request, **kwargs):
    if request.method == "GET":
        board_name = kwargs['board_name']
        board_id = kwargs['board_id']
        if request.user.is_authenticated is True:
            return render(request, "./board/panel.html",  {"board_name":board_name, "board_id":board_id, "user":request.user})
        return render(request, "./board/panel.html",  {"board_name":board_name, "board_id":board_id, "user":None})
        
@csrf_exempt
def loadboard(request):
    board_info = []
    if request.method == "POST":
        board_id = request.POST['board_id']
        user = get_user(request)
        board = UserBoardId.objects.get(id = board_id)

        notes = Note.objects.filter(board = board)
        for note in notes:
            note_info = {
                "title":note.title,
                "comment":note.comment,
                "color":note.color,
                "background_color":note.background_color,
                "board_id":note.note_id,###############
            }
            board_info.append(note_info)
        
        str_board_info = json.dumps(board_info)
        return HttpResponse(str_board_info)
        

def get_user(request):
    user_id = request.user
    user = User.objects.get(username = user_id)
    return user

