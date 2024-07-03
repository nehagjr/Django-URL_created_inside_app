from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Student
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

def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get("name")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    password=request.POST.get("password")
    re_password=request.POST.get("re_password")
    # print(name,email,phone,password,re_password)

    Student.objects.create(Name=name,Email=email,Contect=phone,Password=password,Re_Password=re_password)
    print("Data saved")


