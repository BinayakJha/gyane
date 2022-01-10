from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import *
from markdownx.widgets import AdminMarkdownxWidget
# from .models import QuillPost
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
}

# admin.site.register(EditProfileForm, MyModelAdmin)
admin.site.register(Question, MyModelAdmin)
admin.site.register(Comment, MyModelAdmin)
admin.site.register(profilepic, MyModelAdmin)
