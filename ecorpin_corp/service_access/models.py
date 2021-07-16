import datetime
from django.db import models

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



# Project development phases model
class DevelopmentPhase(models.Model):
    name = models.CharField(max_length=100)

# service project model 
class ServiceProject(models.Model):
    #username = ''
    #service_id = ''
    project_title = models.CharField(max_length=100)
    #start_date = ''
    #deadline = ''
    live_server_url = models.URLField(blank=True)
    static_url = models.URLField(blank=True)
    #contact_details = ''
    payment_info = ''
    technology = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    platform = models.CharField(max_length=100)
    development_phase = models.ForeignKey(DevelopmentPhase, on_delete=models.CASCADE)
    progress = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

