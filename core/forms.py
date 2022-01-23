from dataclasses import field
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django_editorjs_fields import EditorJsWidget

class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user', 'slug', 'views', 'time_st', 'note_editorjs_text','likes']
        widgets = {
            'question': EditorJsWidget(config={'minHeight': 100}),
            'question': EditorJsWidget(
                 plugins=[
            "@editorjs/header",
            "@editorjs/image",
            "@editorjs/quote",
            "@editorjs/list",
            "@editorjs/link",
            "@editorjs/code",
            '@editorjs/embed',
            "@editorjs/table@2.0.1",
            "editorjs-hyperlink",
            "@editorjs/inline-code",
            "@editorjs/marker",
        ],
        tools={
            "Hyperlink": {
                "class": "Hyperlink",
                "config": {
                    "shortcut": 'CMD+L',
                    "target": '_blank',
                    "rel": 'nofollow',
                    "availableTargets": ['_blank', '_self'],
                    "availableRels": ['author', 'noreferrer'],
                    "validate": False,
                }
            },
        },
        ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': EditorJsWidget(config={'minHeight': 100}),
            'comment': EditorJsWidget(
                    plugins=[
                "@editorjs/header",
                "@editorjs/image",
                "@editorjs/quote",
                "@editorjs/list",
                "@editorjs/link",
                "@editorjs/code",
                "@editorjs/embed",
                "@editorjs/table@2.0.1",
            "editorjs-hyperlink",
            "@editorjs/inline-code",
            "@editorjs/marker",
        ],
        tools={
            "Hyperlink": {
                "class": "Hyperlink",
                "config": {
                    "shortcut": 'CMD+L',
                    "target": '_blank',
                    "rel": 'nofollow',
                    "availableTargets": ['_blank', '_self'],
                    "availableRels": ['author', 'noreferrer'],
                    "validate": False,
                }
            },
        },
        ),
        }

# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ['reply']
        
class EditProfileForm(forms.ModelForm):
    small_intro = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=False)
    class Meta:
        model = Profile
        fields = ('small_intro','profile_pic','web','github_username','Twitter_username','instagram_username','Facebook_username')

class EditPersonalProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('email','first_name','last_name','username')