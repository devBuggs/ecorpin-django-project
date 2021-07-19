from django.db import models
import datetime

# Create your models here.

'''
class ProjectsDetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    framework = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(url_name, name=self.name)
''' 

class ClientReview(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    msg = models.CharField(max_length=600)
    
