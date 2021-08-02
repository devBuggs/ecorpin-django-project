import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

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

# extending existing User model into ServiceUser for seperate active ecorpin service user 
class ServiceUser(models.Model):
    user = models.OneToOneField(User, related_name='service_user', on_delete=models.CASCADE)
    service_id = models.CharField(max_length=12, unique=True, blank=False)
    
    def __str__(self):
        return "{}".format(self.service_id)

# class for default development phases (Initiating, Planning, Design, Development, Testing, Production)
class DevelopmentStatus(models.Model):
    phase_name = models.CharField(max_length=50)

    def __str__(self):
        return "{} Phase".format(self.phase_name)

#class for default Status (Active or Inactive)
class ServiceStatus(models.Model):
    status_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.status_name

# class for user services
class Service(models.Model):
    service_id = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=15, blank=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True)
    technology = models.CharField(max_length=50, blank=True)
    framework = models.CharField(max_length=50, blank=True)
    platform = models.CharField(max_length=50, blank=True)
    live_url = models.URLField(blank=True)
    payment_status = models.CharField(max_length=50, blank=True) # need focus
    development_phase = models.OneToOneField(DevelopmentStatus, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(ServiceStatus, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(default=timezone.now)
    deadline = models.DateField(blank=True)
    dedicatedTime = models.IntegerField()
    notification = models.CharField(max_length=150, default=None, blank=True)

    def __str__(self):
        #return "{}".format(self.service_id.service_id)
        return "{}".format(self.title)