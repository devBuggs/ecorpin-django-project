from django.contrib import admin

from .models import spotlight
from .models import endpoint_info
from .models import ecorpian

# Register your models here.
admin.site.register(spotlight)

admin.site.register(endpoint_info)

admin.site.register(ecorpian)