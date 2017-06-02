from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

# Create your models here.
class TeamManager(models.Manager):
    def create_team(self, postData):
        flag = True
        if (len(postData['team_name']) < 1):
            flag=False
        if flag:
            print "Adding team to database"
            Team.objects.create(name = postData['team_name'])
            return True
        else:
            return False

class Team(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = TeamManager()

class User_Team(models.Model):
    team = models.ForeignKey(Team, related_name="team_name")
    user = models.ForeignKey(User, related_name="user_name")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
