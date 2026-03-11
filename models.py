from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class type(models.Model):
    user_email=models.CharField(max_length=50)
    user_name=models.CharField(max_length=30)
    diy_name= models.CharField(max_length=50)
    diy_type= models.CharField(max_length=7)
    diy_material=models.CharField(max_length=500)
    diy_img=models.ImageField(upload_to='uploadedFiles',null=True)

class books(models.Model):
    username=models.CharField(max_length=30, default='default')
    email=models.EmailField(max_length=30,default='example@example.com')
    book_name= models.CharField(max_length=30)
    author_name=models.CharField(max_length=30)
    book_category= models.CharField(max_length=15)
    book_chapter=models.CharField(max_length=10)
    book_pages=models.CharField(max_length=10)
    book_img=models.ImageField(upload_to='uploadedFiles',null=True)
    book_file=models.FileField(upload_to='documents',null=True)

class book(models.Model):
    user=models.ForeignKey(User , on_delete=models.SET_NULL,null=True, blank=True)
    username=models.CharField(max_length=30, default='default')
    email=models.EmailField(max_length=30,default='example@example.com')
    book_name= models.CharField(max_length=30)
    author_name=models.CharField(max_length=30)
    book_category= models.CharField(max_length=15)
    book_chapter=models.CharField(max_length=10)
    book_pages=models.CharField(max_length=10)
    book_img=models.ImageField(upload_to='uploadedFiles',null=True)
    book_file=models.FileField(upload_to='documents',null=True)