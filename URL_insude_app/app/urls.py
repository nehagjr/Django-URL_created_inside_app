from django.urls import path
from .views import home , register
# from app import views

urlpatterns = [
#    path('home/',home),
     path('home/',home),
     path("registration/",register),
]
