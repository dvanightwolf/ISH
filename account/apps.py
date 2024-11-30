from django.apps import AppConfig
from django.core.mail import send_mail


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

