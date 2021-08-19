from django.db import models
from django.contrib.auth.models import User

#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#User = get_user_model


# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transection', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('ECPAY%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


class PaymentDetails(models.Model):
    user = models.ForeignKey(User, related_name='payment', on_delete=models.CASCADE)
    transection_id = models.ForeignKey(Transaction, related_name='transections', on_delete=models.CASCADE)
    txn_id = 'TXN_SUCCESS'
    message = 'message'
    CHECKSUMHASHx = ''
    date_time = ''

    def __str__(self):
        return self.transection_id.order_id
        
