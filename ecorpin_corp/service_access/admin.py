from django.contrib import admin

from .models import TypeReq, ContactRequest, ServiceUser, DevelopmentStatus, ServiceStatus, Service


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('contact_date', 'contact_type', 'contact_status', 'project_title' )
    list_filter = ['contact_status', 'contact_type', 'contact_date', ]

# Register your models here.
#admin.site.register(TypeReq) # Customize AdminModel
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(ServiceUser) # Customize AdminModel
#admin.site.register(DevelopmentStatus) # Customize AdminModel
#admin.site.register(ServiceStatus) # Customize AdminModel
admin.site.register(Service) # Customize AdminModel