from django.contrib.sitemaps import Sitemap
# import reverse
from django.urls import reverse
from .models import *
class Static_Sitemap(Sitemap):
    priority = 1
    changefreq = 'always'
    def items(self):
        return ['home','signup','contact','search']
    def location(self, item):
        return reverse(item)

class Question_Sitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    def items(self):
        return Question.objects.all()
    def location(self, item):
        return reverse('viewnotes', args=[item.note_id])

class Comment_Sitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    def items(self):
        return Comment.objects.all()
    def location(self, item):
        return reverse('viewnotes', args=[item.comment_id])    

class Profile_Sitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    def items(self):
        return Profile.objects.all()
    def location(self, item):
        return reverse('profile', args=[item.user.username])  