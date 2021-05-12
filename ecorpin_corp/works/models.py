from django.db import models
import datetime

# Create your models here.

'''
class ProjectsDetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    ClientName = models.CharField(max_length=100)
''' 

class ClientReview(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    msg = models.CharField(max_length=600)
    
    