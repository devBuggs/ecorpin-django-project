from django.contrib import admin

from .models import spotlight, endpoint_info, ecorpian, feedback

# Register your models here.
admin.site.register(spotlight)

admin.site.register(endpoint_info)

admin.site.register(ecorpian)

admin.site.register(feedback)