import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hatua_Zetu_Foundation.settings')  # Set default settings module

application = get_wsgi_application()  # WSGI application
