from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django_editorjs_fields import EditorJsWidget
# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = EditProfileForm
#         fields = ('bio',)

class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user', 'slug', 'views', 'time_st', 'note_editorjs_text']
        widgets = {
            'note_editorjs': EditorJsWidget(config={'minHeight': 100}),
            'note_editorjs_text': EditorJsWidget(plugins=["@editorjs/image", "@editorjs/header", "@editorjs/list", "@editorjs/marker", "@editorjs/code", "@editorjs/table", "@editorjs/link", "@editorjs/embed","@editorjs/warning","@editorjs/quote","editorjs/delimeter"]),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
class  ProfilePicForm(forms.ModelForm):
    class Meta:
        model = profilepic 
        fields = ['profile_pic']
