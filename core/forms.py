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
            'question': EditorJsWidget(config={'minHeight': 100}),
            'question': EditorJsWidget(
                 plugins=[
            "@editorjs/header",
            "@editorjs/image",
            "@editorjs/quote",
            "@editorjs/list",
            "@editorjs/link",
            "@editorjs/code",
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
class  ProfilePicForm(forms.ModelForm):
    class Meta:
        model = profilepic 
        fields = ['profile_pic']
