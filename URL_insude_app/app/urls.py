from django.urls import path
from .views import *
# from app import views

urlpatterns = [
     path('',home1,name='home'),
     path('home/',home),
     path('about/',about,name='about'),
     path('contect/',contect,name='cotect'),
     path('gallery/',gallery,name='gallery'),
     path('service/',service,name='service'),
     path("registration/",register),
     path("registerData/",registerdata,name='register'),
     path('link/',link),    
]
