from django.apps import AppConfig


# Configure the core app
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default primary key type
    name = 'core'  # App name
