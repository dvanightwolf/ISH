from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "bio", "is_staff"]
