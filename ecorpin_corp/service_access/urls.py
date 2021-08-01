from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url 

# import views here
from . import views

app_name = 'service_access'
urlpatterns = [
    path('contact_request/', views.contact_request, name='contact_request'),
    path('service_login/', views.login_view, name="login"),
    path('dashboard/', views.ServiceDashboard.as_view(), name="dashboard"),
    path('logout/', views.service_logout, name="logout")
]