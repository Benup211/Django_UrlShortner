from django.urls import path
from . import views
app_name="speedylink"
urlpatterns=[
    path('',views.index,name="index"),
]