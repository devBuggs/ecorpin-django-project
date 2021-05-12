from django.urls import path
from . import views

urlpatterns = [
    path('work/', views.projects_view, name='projects'),

]