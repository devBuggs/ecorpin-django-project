from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


# favicon view of the web server
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('favicon.ico', favicon_view),
    path('admin/', admin.site.urls),
    path('', include('ecorpin.urls')),
    path('', include('service_access.urls')),
    path('', include('bbit.urls')),
    path('', include('works.urls')),
    path('', include('payment.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
