from django.urls import path,include
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views
from .views import *
from . import views
# import editprofilepageview

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
    # notes
    path('edit_profile/<str:username>/', UserEditView.as_view(), name='edit_profile'),
    path('edit_personal_profile/', UserProfileEditView.as_view(), name='edit_profile_personal'),
    # profile
    path('profile/<str:username>/', views.UserProfileView, name='profile'),
    path('notes', views.note, name='notes'),
    path('viewnotes/<int:note_id>', views.viewnotes, name='viewnotes'),
    path('editorjs/', include('django_editorjs_fields.urls')), 
    # search
    path('search', views.search, name='search'),
    # likes
    # path('like/<int:note_id>', LikeView , name='like_post'),
    path('like/<int:note_id>', views.like, name='like'),
    # for edit profile

)

