from django.shortcuts import render,redirect
from django.http import HttpResponse

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
        return render(request,'speedylink/signin.html',{})
    else:
        return redirect('speedylink:profile')

def Signup_view(request):
    return HttpResponse("SignUp")