from django.urls import path
from .views import *
# from app import views

urlpatterns = [
#    path('home/',home),
     path('home/',home),
     path("registration/",register),
     path("registerData/",registerdata,name='register'),
     path('link/',link),    
]
