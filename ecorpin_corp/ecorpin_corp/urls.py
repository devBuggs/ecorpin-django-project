from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecorpin.urls')),
    path('', include('service_access.urls')),
    path('', include('block_bit')),
    path('ar/', include('ecorpin_ar')),
    path('vr/', include('ecorpin_vr')),
    path('', include('lab')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
