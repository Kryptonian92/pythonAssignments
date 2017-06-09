from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from django.shortcuts import render, HttpResponse, redirect
from ..login_app.models import User
from datetime import datetime
from django.contrib import messages

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
