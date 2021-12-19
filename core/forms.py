from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = EditProfileForm
#         fields = ('bio',)

class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['note', 'image']

class  ProfilePicForm(forms.ModelForm):
    class Meta:
        model = profilepic 
        fields = ['profile_pic']
