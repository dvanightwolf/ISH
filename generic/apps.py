from django.apps import AppConfig

count = 1


class GenericConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generic'

    def ready(self):
        from generic.views import scheduler
        scheduler()

