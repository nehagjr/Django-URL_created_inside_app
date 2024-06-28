from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
# Create your views here.

def home(response):
    # return HttpResponse("<h1 style='color:red'>Welcome</h1>")
    data={
        "name":"Neha",
        "age":20,
        "sub":"Django"
    }
    return JsonResponse(data)

def register(request):
    return render(request,'register.html')

def link(request):
    return redirect('https://www.github.com/')