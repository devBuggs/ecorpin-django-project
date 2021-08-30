from django.urls import path

from .views import index 

app_name = 'lab'

urlpatterns = [
    path('', index, name="lab_home"),
]