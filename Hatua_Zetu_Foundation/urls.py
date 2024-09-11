from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('core.urls')),  # Core app URLs
    path('donations/', include('donations.urls', namespace='donations')),  # Donations app URLs
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Media files
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),  # Static files
]
