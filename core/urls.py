from django.urls import path,include
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views
from .views import *
from . import views
# import editprofilepageview
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import *

sitemaps = {
    'static': Static_Sitemap,
    'questions': Question_Sitemap,
    'comments': Comment_Sitemap,
    'profiles': Profile_Sitemap,
}


urlpatterns = (
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup_success', views.handleSignUp, name='signup_success'),
    # activate
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),

    path('login_success', views.handleLogin, name="login_success"),

    path('logout/', views.handelLogout, name="handleLogout"),
    # password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='core/forgot-password.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='core/password_reset_form.html'), name='password_reset_confirm'),

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
    path('like/<int:note_id>', views.like, name='like'),
    # edit question
    path('question/edit/<int:pk>', UpdatePostView.as_view(), name='edit_question'),

    path('question/delete/<int:pk>', DeletePostView.as_view(), name='delete_question'),
    # comments
    path('comment/edit/<int:pk>', CommentEdit.as_view(), name='comment'),

    path('comment/delete/<int:pk>', CommentDelete.as_view(), name='delete_comment'),
    # password change
    path('password_change/', PasswordsChangeView.as_view(template_name='core/password_change.html'), name='password_change'),
    # for contact
    path('contact/', views.contact_view, name='contact'),
    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # robots.txt
    path('robots.txt', views.robots, name='robots'),
)

