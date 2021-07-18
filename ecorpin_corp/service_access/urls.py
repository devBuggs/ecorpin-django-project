from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url 

# import views here
from . import views

app_name = 'service_access'
urlpatterns = [
    path('service_access/', views.service_access_view, name='service_access'),
    path('contact_request/', views.contact_request, name='contact_request'),
    path('service_login/', views.service_login_view, name="login"),
]