from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SigninForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    context={}
    return render(request,'speedylink/index.html',context)

def profile(request):
    if request.user.is_anonymous:
        return redirect('speedylink:signin')
    else:
        return HttpResponse("user is online")

def Signin_view(request):
    if request.user.is_anonymous:
        context={}
        if(request.method=="POST"):
            form=SigninForm(request.POST)
            if form.is_valid()==False:
                form=SigninForm()
                context={
                    'error':True
                }
            else:
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                authenticate_user=authenticate(username=username,password=password)
                if authenticate_user is not None:
                    login(request,authenticate_user)
                    return redirect('speedylink:profile')
                else:
                    context={
                    'error':True
                    }
        return render(request,'speedylink/signin.html',context)
    else:
        return redirect('speedylink:profile')

def Signup_view(request):
    if request.user.is_anonymous:
        context={}
        if(request.method=="POST"):
            form=SignupForm(request.POST)
            if form.is_valid()==False:
                form=SigninForm()
                context={
                    'error':True
                }
            else:
                user_registered=False
                users=User.objects.all()
                username=form.cleaned_data['username']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                user=User()
                user.username=username
                user.email=email
                user.is_active=True
                user.is_staff=False
                for indiv_user in users:
                    if (user.username==indiv_user.username):
                        user_registered=True
                if (user_registered==False):
                    user.set_password(password)
                    user.save()
                    return redirect('speedylink:signin')
                else:
                    context={
                    'error':True
                    }

        return render(request,'speedylink/signup.html',context)
    else:
        return redirect('speedylink:profile')