from django.db import models

# Create your models here.
class Student(models.Model):
    Name =models.CharField(max_length=50)
    Email =models.EmailField()
    Contect=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Re_Password=models.CharField(max_length=10)