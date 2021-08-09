
from django.urls import path
from payment import views

app_name = 'payment'
urlpatterns = [
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('paymentinfo/', views.paymentCallback, name='payment_info'),

]