from django.urls import path
# from .views import home
from app import views

urlpatterns = [
#    path('home/',home),
     path('home/',views.home)
]
