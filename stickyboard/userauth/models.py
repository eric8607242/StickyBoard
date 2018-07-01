from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Profile(models.Model):
    #使用者註冊需要多輸入的資料
    #When the referenced object is deleted, also delete the objects that have references to it 
    user = models.OneToOneField(User,related_name = 'user_profile',on_delete=models.CASCADE)

class UserBoardId(models.Model):
    #板子內部所需要的資訊
    board_name = models.CharField(max_length = 20)
    user = models.ManyToManyField(
        User,related_name = 'userboardid'
    )
    
    



#form type
class UserForm(UserCreationForm):
    username = forms.CharField(label='Username',max_length = 100)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',max_length = 100)
    password2 = forms.CharField(label='Password(confirm)',max_length = 100)
    class Meta:
        #可有可無,因為default已經設成User
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    test = forms.CharField(label="測試",max_length = 100)
    class Meta:
        model = Profile
        fields = ['test']


class Note(models.Model):                                                          
    board = models.ForeignKey(UserBoardId, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    comment = models.TextField(max_length=800)
    color = models.TextField(max_length=10)
    background_color = models.TextField(max_length=10)    

