from django.contrib import admin
from .models import Profile


# Register the profile model to the admin site
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "bio", "picture"]
