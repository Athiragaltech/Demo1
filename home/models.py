from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    desig=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
 
