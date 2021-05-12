from django.contrib import admin

from .models import ClientReview

class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'email')
    list_filter = ['company']


# Register your models here.

admin.site.register(ClientReview, ClientReviewAdmin)