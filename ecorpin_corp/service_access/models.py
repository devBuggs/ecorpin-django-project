import datetime
from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class TypeReq(models.Model):
    medium = models.CharField(max_length=20)

    def __str__(self):
        return self.medium

class ContactRequest(models.Model):
    project_title = models.CharField(max_length=200)
    project_idea = models.TextField()
    contact_date = models.DateTimeField('Contact Date')
    contact_email = models.EmailField(max_length=200)
    contact_mobile = models.IntegerField()
    contact_name = models.CharField(max_length=100)
    contact_type = models.ForeignKey(TypeReq, on_delete=models.CASCADE)
    contact_status = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title


'''
class ServiceUser(auth.models.User, auth.models.PermissionsMixin):

    def __str__():
        return "@{}".format(self.username)

# Project development phases model
class DevelopmentPhase(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# service project model 
class ServiceProject(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    service_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True)
    technology = models.CharField(max_length=50)
    framework = models.CharField(max_length=50)
    platform = models.CharField(max_length=100)
    development_phase = models.ForeignKey(DevelopmentPhase, on_delete=models.CASCADE)
    progress = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    live_url = models.URLField(blank=True)
    static_url = models.URLField(blank=True)
    payment_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.service_id

'''

