from django.db import models

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
