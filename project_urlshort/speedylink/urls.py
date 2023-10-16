from django.urls import path
from . import views
app_name="speedylink"
urlpatterns=[
    path('',views.index,name="index"),
    path('profile/',views.profile,name="profile"),
    path('Signin/',views.Signin_view,name="signin"),
    path('Signup/',views.Signup_view,name="signup"),
]