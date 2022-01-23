from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
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
    first_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    small_intro = models.TextField(max_length=100, blank=True, null=True)
    web = models.URLField(max_length=200, blank=True, null=True)
    github_username = models.CharField(max_length=200, blank=True, null=True)
    Twitter_username = models.CharField(max_length=200, blank=True, null=True)
    Facebook_username = models.CharField(max_length=200, blank=True, null=True)
    instagram_username = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(default="defaultprofile_photo.png", null=True, blank=True)

    
    def __str__(self):
        return str(self.user)
class Question(models.Model):
    note_id = models.AutoField(primary_key=True)
    question =EditorJsJSONField(readOnly=False, autofocus=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now_add=True)
    profile_pic = property(lambda self: self.user.profile.profile_pic)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    views  = models.IntegerField(default=0)
    total_comments = property(lambda self: self.comment_set.count())
    # remove word Comment from comments
    # get the first comment 
    def get_first_comment(self):
        return self.comment_set.all()[:1].get()
    comment = get_first_comment
    # remove word 'Comment' from comment
    


    @property
    def total_likes(self):
        return self.likes.count()
    
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
    questionid = property(lambda self: self.question_set.note_id)
    time_st = models.DateTimeField(auto_now_add=True)
    views  = models.IntegerField(default=0)
    profile_pic = property(lambda self: self.user.profile.profile_pic)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.comment)
        super(Comment, self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user.username)

# class Reply(models.Model):
#     reply_id = models.AutoField(primary_key=True)
#     reply = models.TextField(max_length=200, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     time_st = models.DateTimeField(auto_now_add=True)
#     views  = models.IntegerField(default=0)
#     profile_pic = property(lambda self: self.user.profile.profile_pic)
    
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.reply)
#         super(Reply, self).save(*args, **kwargs)
    
#     def __str__(self):
#         return 'Reply {} by {}'.format(self.reply, self.user.username)
class Updates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    update_title = models.CharField(max_length=200, null=True)
    update = models.TextField()
    link = models.URLField(max_length=200, null=True)
    time_st = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.update_title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    content=models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def get_object(self):
        return self.email
    def __str__(self):
        return 'Message From '+' - '+self.email

