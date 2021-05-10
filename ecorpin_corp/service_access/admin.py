from django.contrib import admin

from .models import TypeReq, ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('contact_date', 'contact_type', 'contact_status', 'project_title' )
    list_filter = ['contact_status', 'contact_type', 'contact_date', ]

# Register your models here.
#admin.site.register(TypeReq)
admin.site.register(ContactRequest, ContactRequestAdmin)