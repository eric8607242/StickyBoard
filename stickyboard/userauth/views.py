from django.shortcuts import render
from django.http import HttpResponse

from .models import ProfileForm ,UserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)

        if userform.is_valid() and profileform.is_valid():
    
            #use commit=False,it will return an object that hasn’t yet been saved to the database.
            user = userform.save()
            profileform = profileform.save(commit=False)
            
            profileform.user = user
            profileform.save()

            #利用剛剛存入db的return user登入
            if user is not None:
                login(request,user)

            return HttpResponse("success")
        return HttpResponse("failed")

    else:
        userform = UserForm()
        profileform = ProfileForm()

    return render(request,"./userauth/signup.html",{'userform':userform,'profileform':profileform})


