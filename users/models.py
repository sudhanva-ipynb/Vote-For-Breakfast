from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User

from django.contrib.auth import get_user

# Create your models here.
class BreakFast(models.Model):
    id=models.IntegerField(primary_key=True)
    mealname=models.CharField(max_length=30)
    voteCount=models.IntegerField(default=0)
    def __str__(self):
        return "%d) %s " % (self.id, self.mealname)  

class Voted(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=30)
    timeVoted=models.DateTimeField(default=datetime.utcnow())


