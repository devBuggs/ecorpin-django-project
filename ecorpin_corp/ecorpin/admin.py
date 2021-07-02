from django.contrib import admin

from .models import Spotlight, Endpoint_info, Ecorpian, Feedback, EcorpinStat

class SpotlightAdmin(admin.ModelAdmin):
    list_display = ('spotlight_date', 'spotlight_info')

class EcorpianAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name', 'email', 'office_address')
    list_filter = ['office_address']

class Endpoint_infoAdmin(admin.ModelAdmin):
    list_display = ('end_point', 'sideNav', 'title')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'visitor_organization', 'visitor_email')

class EcorpinStatAdmin(admin.ModelAdmin):
    list_display = ('client_stat', 'project_stat', 'service_stat')

# Register your models here.
admin.site.register(Spotlight, SpotlightAdmin)
admin.site.register(Endpoint_info, Endpoint_infoAdmin)
admin.site.register(Ecorpian, EcorpianAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(EcorpinStat, EcorpinStatAdmin)