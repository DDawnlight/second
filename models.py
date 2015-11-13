from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class People(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    number = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    qq = models.CharField(max_length=10)
    birth = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    
    

    
   
