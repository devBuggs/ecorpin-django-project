from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# import views here
from . import views

urlpatterns = [
    path('service_access/', views.service_access_view, name='service_access'),
    path('contact_request', views.contact_request, name='contact_request'),
]