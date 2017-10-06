# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import re

alpha = re.compile(r'^[a-z A-Z]*$')
regexPw = re.compile(r'^[a-z A-Z 0-9]*$')
# regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, postData):
        error = []
        flag = True
        if not User.objects.filter(username = postData['username']):
            flag = False
            error.append('You have not registered')
        if (len(postData['password']) < 9) and (len(postData['password']) > 1):
            flag=False
            error.append("Password Is Too Short")
            print "Password is too short"
        if (len(postData['password']) < 1):
            flag=False
            error.append("You did not enter a password")
        if not regexPw.match(postData['password']):
            flag = False
            error.append("Invalid Format. Your password must have letters")
        if (len(postData['username']) < 1):
            flag = False
            error.append("You did not enter a Username")
        if (len(postData['username']) < 4) and (len(postData['username']) > 1):
            flag = False
            error.append("Username is too short")
        if flag:
            return True
        else:
            return False, error

    def register(self, postData):
        error = []
        flag = True
        if User.objects.filter(username = postData['username']):
            flag = False
            error.append('You have already registered. Please Login')
        if (len(postData['password']) < 9) and (len(postData['password']) > 1):
            flag=False
            error.append("Password Is Too Short")
            print "Password is too short"
        if (len(postData['password']) < 1):
            flag=False
            error.append("You did not enter a password")
        if not regexPw.match(postData['password']):
            flag = False
            error.append("Invalid Format. Your password must have letters")
        if (len(postData['username']) < 1):
            flag = False
            error.append("You did not enter a Username")
        if (len(postData['username']) < 4) and (len(postData['name']) > 1):
            flag = False
            error.append("Username is too short")
        if (len(postData['name']) < 1):
            flag = False
            error.append("You did not enter a name")
        if (len(postData['name']) < 4) and (len(postData['name']) > 1):
            flag = False
            error.append("Name is too short")
        if not (postData['password']) == (postData['pwconfirm']):
            flag=False
            error.append("Your confirmation does not match your password")
        if flag:
            User.objects.create(name = postData['name'], username = postData['username'], password = postData['password'])
            return True
        else:
            return False, error

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length =45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
  # *************************
  # Connect an instance of UserManager to our User model overwriting
  # the old hidden objects key with a new one with extra properties!!!

    objects = UserManager()

  # *************************

class TripManager(models.Manager):
    def new_trip(self, postData, newUser):
        error = []
        flag = True
        if len(postData['destination']) < 1:
            error.append('Destination cant be blank')
            flag = False
        if Trip.objects.filter(destination = postData['destination']):
            error.append('TRIP ALREADY EXISTS!')
            flag = False
        if postData['travel_to'] < postData['travel_from']:
            error.append('TRIP END MUST BE AFTER START!')
            return (False, error)
        if flag:
            Trip.objects.create(created_by = newUser ,  destination = postData['destination'], travel_start = postData['travel_from'], travel_end = postData['travel_to'], description = postData['description'])
            return True
        else:
            return False, error

class Trip(models.Model):
    # user = models.ForeignKey(User, related_name = "now_user")
    destination = models.CharField(max_length=255)
    # created_by = models.ForeignKey(User, related_name = "user_now")
    created_by = models.CharField(max_length = 255)
    travel_start = models.DateField(auto_now = False)
    travel_end = models.DateField(auto_now = False)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
    # def __str__(self):
    #     return self.name

class User_Trip(models.Model):
    trips = models.ForeignKey(Trip, related_name="new_trips")
    users = models.ForeignKey(User, related_name="users_name")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
