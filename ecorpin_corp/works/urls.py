from django.urls import path
from . import views

#app_name = 'works'
urlpatterns = [
    path('work/', views.projects_view, name='projects'),

]