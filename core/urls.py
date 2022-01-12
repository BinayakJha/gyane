from django.urls import path,include
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup_success', views.handleSignUp, name='signup_success'),
    path('login_success', views.handleLogin, name="login_success"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='core/forgot-password.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='core/password_change.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('edit_profile', UserEditView.as_view(), name="edit_profile"),
    # notes
    path('notes', views.note, name='notes'),
    # path('comments', views.add_comment, name='comments'),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('viewnotes/<int:note_id>', views.viewnotes, name='viewnotes'),
    # comment
    # add coment
    
    # path('comment/<int:note_id>', views.comment, name='comment'),
    # for opening  note 
    # path('note/<int:pk>/', views.note_detail, name='note_detail'),
    
)
