from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_details(models.Model):
    user1=models.ForeignKey(User,on_delete=models.CASCADE)
    about=models.TextField(max_length=50,null=True,blank=True)
    images=models.ImageField(upload_to='images/',null=True,blank=True)

def __str__(self):
    return self.user


class membership(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    val=models.IntegerField(null=False,blank=False)

def __str__(self):
    return self.name 

class addmembership(models.Model):
    user2=models.ForeignKey(User,on_delete=models.CASCADE)
    member=models.ForeignKey(membership,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.user2

class landingpage(models.Model):
    image=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)

class feedback(models.Model):
    user3=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=50,null=False,blank=False)
    date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.user3