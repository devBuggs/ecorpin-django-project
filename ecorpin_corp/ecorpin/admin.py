from django.contrib import admin

from .models import spotlight, endpoint_info, ecorpian, feedback, EcorpinStat

class spotlightAdmin(admin.ModelAdmin):
    list_display = ('spotlight_date', 'spotlight_info')

class ecorpianAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name', 'email', 'office_address')
    list_filter = ['office_address']

class endpoint_infoAdmin(admin.ModelAdmin):
    list_display = ('end_point', 'sideNav', 'title')

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'visitor_organization', 'visitor_email')

class EcorpinStatAdmin(admin.ModelAdmin):
    list_display = ('client_stat', 'project_stat', 'service_stat')

# Register your models here.
admin.site.register(spotlight, spotlightAdmin)
admin.site.register(endpoint_info, endpoint_infoAdmin)
admin.site.register(ecorpian, ecorpianAdmin)
admin.site.register(feedback, feedbackAdmin)
admin.site.register(EcorpinStat, EcorpinStatAdmin)