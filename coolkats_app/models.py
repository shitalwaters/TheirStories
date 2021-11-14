from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True)
    story=models.TextField(blank=True)
    web_link = models.CharField(max_length=200, null=True)
    image = models.TextField(blank=True)
    fields=models.CharField(max_length=350, null=True)
    motivations=models.CharField(max_length=350, null=True) 

class AvailableTime(models.Model):
    mentor=models.ForeignKey(Mentor, null=True, on_delete=models.PROTECT)
    startTime=models.DateTimeField( null=True)
    endTime=models.DateTimeField( null=True)
    duration=models.IntegerField(default=30, null=False)
    title=models.TextField(blank=True)
    user=models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)