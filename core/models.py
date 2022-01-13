from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from markdownx.models import MarkdownxField
from django.utils.text import slugify
from django_editorjs_fields import EditorJsJSONField  # Django >= 3.1
from django_editorjs_fields import EditorJsTextField
import core

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()

# class EditProfileForm(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     # gender = models.CharField(choices=GENDER_CATEGORY,max_length=2)
#     profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
#     bio = MarkdownxField(null=True, blank=True)

#     def __str__(self):
# 	    return self.first_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # import first name from user
    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        super(Profile, self).save(*args, **kwargs)
    first_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    small_intro = models.TextField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(default="defaultprofile_photo.png", null=True, blank=True)

    def __str__(self):
        return str(self.user)
class Question(models.Model):
    note_id = models.AutoField(primary_key=True)
    question =EditorJsJSONField(readOnly=False, autofocus=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now_add=True)
    # join the Profile.profile_pic fiels to profile
    profile_pic = property(lambda self: self.user.profile.profile_pic)
       
    views  = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        # self.slug = slugify(self.clean)
        super(Question, self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Question {} by {}'.format(self.question, self.user.username)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment =  EditorJsJSONField(readOnly=False, autofocus=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now_add=True)
    views  = models.IntegerField(default=0)
    profile_pic = property(lambda self: self.user.profile.profile_pic)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.comment)
        super(Comment, self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user.username)

