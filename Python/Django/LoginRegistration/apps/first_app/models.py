# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import re

alpha = re.compile(r'^[a-zA-Z]*$')
regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def login(self, postData):
        error = []
        flag = True
        if (len(postData['password']) < 8) and (len(postData['password']) > 1):
            flag=False
            error.append("Password Is Too Short")
            print "Password is too short"
        if (len(postData['password']) < 1):
            flag=False
            error.append("You did not enter a password")
        if (len(postData['email']) < 1):
            flag = False
            error.append("You did not enter a password")
        if (len(postData['email']) < 8) and (len(postData['email']) > 1):
            flag = False
            error.append("Email is too short")
        if not regex.match(postData['email']):
            flag = False
            error.append("Invalid email format")
        if flag:
            return True
        else:
            return False, error

    def register(self, postData):
        error = []
        flag = True
        if (len(postData['first_name']) < 3) and (len(postData['first_name']) > 1):
            flag=False
            error.append("First name is too short")
        if (len(postData['first_name']) < 1):
            flag=False
            error.append("You did not enter your first name")
        if not alpha.match(postData['first_name']):
            flag=False
            error.append("First name is Invalid. Letters Only")
        if (len(postData['last_name']) < 3) and (len(postData['last_name']) > 1):
            flag=False
            error.append("Last name is too short")
        if (len(postData['last_name']) < 1):
            flag=False
            error.append("You did not enter your last name")
        if not alpha.match(postData['last_name']):
            flag=False
            error.append("Last name is invalid. Enter letters only")
        if (len(postData['email']) < 1):
            flag=False
            error.append("You did not enter an email")
        if not regex.match(postData['email']):
            flag=False
            error.append("Invalid email format")
        if (len(postData['password']) < 8) and (len(postData['password']) > 1):
            flag=False
            error.append("Password is too short")
        if (len(postData['password']) < 1):
            flag=False
            error.append("You did not enter a password")
        if not (postData['password']) == (postData['pwconfirm']):
            flag=False
            error.append("Your confirmation does not match your password")
        if flag:
            return True
            User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = postData['password'])
        else:
            return False, error

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length =45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
  # *************************
  # Connect an instance of UserManager to our User model overwriting
  # the old hidden objects key with a new one with extra properties!!!

    objects = UserManager()

  # *************************
