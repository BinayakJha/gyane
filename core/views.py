from pyexpat import model
from django import template
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, request, JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
# email
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context, context
import math, random,json

from django_editorjs_fields import fields

from .models import Profile, Updates, UserOTP,Question,Comment

from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.views import generic
from django.views.generic import CreateView,UpdateView, DeleteView
from .forms import EditPersonalProfileForm, NoteForm,CommentForm,EditProfileForm
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
# edit profile page class

class UpdatePostView(UpdateView):
   model = Question
   form_class = NoteForm
   template_name = 'core/updatequestion.html'
#    fields = ['question']
   success_url = reverse_lazy('home')

# DELETE A POST
class DeletePostView(DeleteView):
    model = Question
    template_name = 'core/delete_post.html'
    success_url = reverse_lazy('home')
# COMMENT EDIT AND DELETE
class CommentEdit(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'core/commentedit.html'
    success_url = reverse_lazy('home')

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'core/comment_delete.html'
    success_url = reverse_lazy('home')
# ------------------------------------------------------------------------------------
# 404 page
# ------------------------------------------------------------------------------------
def page_not_found_view(request, exception):
    return render(request, 'core/404.html', status=404)
# ------------------------------------------------------------------------------------
# edit profile page class
# ------------------------------------------------------------------------------------
class UserProfileEditView(generic.UpdateView):
    form_class = EditPersonalProfileForm
    template_name = 'core/edit_personal.html'
    def get_success_url(self):
        return reverse_lazy('edit_profile', kwargs={'username': self.request.user.username})

    def get_object(self):
        return self.request.user
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'core/edit_profile.html'
    # if succes remain in the same page
    def get_success_url(self):
        return reverse_lazy('edit_profile', kwargs={'username': self.request.user.username})


    def get_object(self):
        return self.request.user.profile

    
# ------------------------------------------------------------------------------------
# user profile 
# ------------------------------------------------------------------------------------
def UserProfileView(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    quest = Question.objects.filter(user=user)
    ans = Comment.objects.filter(user=user)
    context = {
        'user': user,
        'profile': profile,
        'quest': quest,
        'ans': ans,
    }
    return render(request, 'core/profile.html', context)
# ------------------------------------------------------------------------------------
# home function
# ------------------------------------------------------------------------------------

def home(request):
    # return render(request, 'core/login.html')
    # order by views
    postss = Question.objects.all().order_by('-time_st')
    p = Paginator(postss, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    up = Updates.objects.all().order_by('-time_st')
    # filter comment for each post
    form = NoteForm()
    context = {'postss':postss,
                'form':form,
                'page_obj': page_obj,
                'updates': up,
    }
    return render(request, 'core/login.html', context)


def signup(request):
    return render(request, 'core/register.html')

def verify(request):
   return render(request, 'core/token_verify.html')
        
def forgot_password(request):
    return render(request, 'core/forgot-password.html')

def home_logged(request):
    return render(request, 'core/home.html')
# ------------------------------------------------------------------------------------
# signup function
# ------------------------------------------------------------------------------------

def handleSignUp(request):  # sourcery no-metrics
    if request.method == "POST":
        # Get the post parameters
        get_otp = request.POST.get('otp')
        
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.is_staff = True
                usr.save()
                messages.success(request, "Account Activated")
                template1 = get_template('core/welcome_email.html').render({'name': usr.username})
                subject = 'Thankyou For Joining Gyan-e Team.'
                email = EmailMessage(
                    subject,
                    template1,
                    settings.EMAIL_HOST_USER,
                    [usr.email, ],

                )
                email.fail_silently = False
                email.content_subtype = "html"
                email.send()
                return redirect("home")

            else:
                messages.error(request, "Invalid OTP")
                return render(request, 'core/register.html',{'otp':True, 'usr':usr})
        usernames = request.POST['username']
        
        email = request.POST['email']
        fname = request.POST['first_name']
        lname= request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password_repeat']
       
        

        # check if user/email already exsist or not

        if User.objects.filter(username=usernames).exists() and User.objects.filter(email=email).exists():
            messages.error(request, "Email and username already exsist.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, " Email already exsist.")
            return redirect('signup')

        if User.objects.filter(username=usernames).exists():
            messages.error(request, " Username already exsist.")
            return redirect('signup')

        # check for errorneous input

        if len(usernames) < 3:
            messages.error(
                request, " Your username must be under 10 characters")
            return redirect('signup')

        if not usernames.isalnum():
            messages.error(
                request, " Username should only contain letters and numbers")
            return redirect('signup')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        emails = authenticate(email=email)
        if emails is not None:
            messages.error(
                request, "Email you entered already exists. Please login or use different email")
            return redirect("signup")
        is_staff = True
        # Create the user
        myuser = User.objects.create_user(usernames, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_staff = False
        myuser.is_active = False
        # create user profile
        myuser.save()

        # send otp

        myuser_otp = random.randint(100000, 999999)
        UserOTP.objects.create(user=myuser, otp=myuser_otp)
        template2 = get_template('core/token.html').render({ 'myuser_otp':myuser_otp})
        email_otp = EmailMessage (
            'Your OTP',
            template2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email_otp.fail_silently = False
        email_otp.content_subtype = "html"
        email_otp.send()
        # make profile
        myprofile = Profile(user=myuser)
        myprofile.save()

        return render(request, 'core/register.html', {'otp': True, 'usr':myuser})
       
       
    else:
        return HttpResponse("404 - Not found")

# ------------------------------------------------------------------------------------
# login function
# ------------------------------------------------------------------------------------

def handleLogin(request): 
    if request.method=="POST":
        # Get the post parameters
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginemail, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
        
    else:
        return HttpResponse("404- Not found")

# ------------------------------------------------------------------------------------
# logout function
# ------------------------------------------------------------------------------------

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

# ------------------------------------------------------------------------------------
# password change 
# ------------------------------------------------------------------------------------

def password_success(request):
    # return render (request,'registration/password_success.html')
    messages.success(request, "Password has been succesfully changed.")
    return redirect("home")

# ------------------------------------------------------------------------------------
# note function
# ------------------------------------------------------------------------------------
def note(request):
    if request.method == "POST":
        # Get the post parameters
        form = NoteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            # note_html = markdownify.markdownify(form.cleaned_data['note'])
            # # convert it  to markdown
            # print(note_html)
            form.instance.note = form.cleaned_data['question']
            form.save()
            return JsonResponse({'bool':True})
        else:
            messages.error(request, "Note has not been added")
            return redirect("home")
    else:
        form = NoteForm()
        return render(request, 'core/login.html',{'form':form})

# ------------------------------------------------------------------------------------
# view question
# ------------------------------------------------------------------------------------

def viewnotes(request,note_id):
    context = {}
    note = Question.objects.get(note_id=note_id)
    postss = Question.objects.filter(note_id=note_id)
    note.views += 1
    note.save()

    commentt = Comment.objects.filter(question = note).order_by('-time_st')
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comm = request.POST.get('comment')
            f = Comment.objects.create(user=request.user, comment=comm, question=note)
            f.save()
            
        else:
            print("error")
        return redirect('viewnotes',note_id=note_id)
    else:
        form = CommentForm()
        context = {
            'note': note,
            'postss': postss,
            'form': form,
            'comment': commentt,
            'title': Question.objects.get(note_id=note_id).question,
        }
        template_name = 'core/viewnotes.html'
        return render(request, template_name, context)

# ------------------------------------------------------------------------------------
# password change view
# ------------------------------------------------------------------------------------
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'core/password_change.html'
    success_url = reverse_lazy('password_success')

# ------------------------------------------------------------------------------------
# search function
# ------------------------------------------------------------------------------------

def search(request):
    if request.method == "GET":
        searched = request.GET['searched']
        # transform json to simple string
        query = Question.objects.filter(question__icontains = searched)
        return render(request, 'core/search.html',{'searched': searched,'queries':query})
    else:
        return render(request, 'core/search.html',{})
    

def like(request,note_id):
    if request.method == 'POST':
        user = request.user
        question = get_object_or_404(Question, note_id=note_id)
        if user in question.likes.all():
            question.likes.remove(user)
            message = 'unliked'
        else:
            question.likes.add(user)
            message = 'liked'
        ctx = { 'likes_count': question.total_likes , 'message': message}
        return HttpResponse(json.dumps(ctx), content_type='application/json')
