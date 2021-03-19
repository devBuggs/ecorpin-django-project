import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
#----------------------------S-P-O-T-L-I-G-H-T
class spotlight(models.Model):
    spotlight_info = models.CharField(max_length=600)
    spotlight_text = models.CharField(max_length=600)
    spotlight_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.spotlight_info
    
    def was_published_recently(self):
        return self.spotlight_date >= timezone.now() - datetime.timedelta(days=1)

#----------------------------E-N-D-P-O-I--N-T
class endpoint_info(models.Model):
    title = models.CharField(max_length=20)
    end_point = models.CharField(max_length=50)
    sideNav = models.CharField(max_length=20)
    main_headBox = models.CharField(max_length=500)
    edge_headBox = models.CharField(max_length=200)
    
    def __str__(self):
        return self.end_point

#----------------------------E-C-O-R-P-I-A-N
class ecorpian(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    office_address = models.CharField(max_length=100)
    message = models.TextField()
    joinDate = models.DateTimeField('Joining Date')
    
    def __str__(self):
        return self.name

#----------------------------F-E-E-D-B-A-C-K
class feedback(models.Model):
    visitor_name = models.CharField(max_length=50)
    visitor_organization = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    feedback_msg = models.TextField()

    def __str__(self):
        return self.visitor_email

#----------------------------N-E-W_P-R-O-J-E-C-T



#----------------------------C-O-N-T-A-C-T_T-Y-P-E
