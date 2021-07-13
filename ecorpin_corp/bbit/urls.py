from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bbit'
urlpatterns = [
    path('block_bit/', views.index_bbit, name='bbit'),
]