from django.contrib import admin
# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('note_id','question','user','views')
admin.site.register(Question,PostAdmin)
admin.site.register(Comment)
# admin.site.register(Reply)
admin.site.register(Profile)
admin.site.register(Updates)
