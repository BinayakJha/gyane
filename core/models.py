from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from markdownx.models import MarkdownxField
from django.utils.text import slugify
# Create your models here.

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()

class EditProfileForm(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    bio = MarkdownxField(null=True, blank=True)

    def __str__(self):
	    return self.first_name

class Question(models.Model):
    note_id = models.AutoField(primary_key=True)
    note =  MarkdownxField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user first name
    
    time_st = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=200, unique=True)
    views  = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.note)
        super(Question, self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Question {} by {}'.format(self.note[:50], self.user.username)



# class QuillPost(models.Model):
#     content = QuillField()

# quillpost
