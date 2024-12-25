from django.urls import path
from .views import *
urlpatterns = [
    path('index',index,name="index"),
    path('homepage',homepage,name="homepage"),
    path('',handbook,name="handbook"),
]