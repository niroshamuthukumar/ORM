from django.db import models
from django.contrib import admin
class Book(models.Model):
   serialno=models.IntegerField(primary_key=True);
   Bookname=models.CharField(max_length=30);
   Author=models.CharField(max_length=20);
   publishedDate=models.DateField();
   Booktype=models.CharField(max_length=20);
class BookAdmin(admin.ModelAdmin):
   list_display=("serialno","Bookname","Author","publishedDate","Booktype");


