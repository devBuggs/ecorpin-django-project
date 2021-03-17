from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index_ecorpin, name='index'),
    path('test', views.test, name='test'),

    
    path('about', views.about, name='about'),
    path('careers', views.careers, name='careers'),
    path('contact', views.contact, name='contact'),
    path('terms_of_use', views.tou, name='tou'),
    path('team', views.team, name='team'),
    path('privacy', views.privacy, name='privacy'),
    path('server_maintenance', views.maintenance, name='maintenance'),
    path('covid', views.covid, name='covid')
]