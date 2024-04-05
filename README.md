# Ex02 Django ORM Web Application
## Date: 07/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](BOOK.png)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)

models.py

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
```
## OUTPUT

![alt text](<Screenshot 2024-04-05 090836.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
