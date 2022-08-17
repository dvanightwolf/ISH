from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

Gender = (
    ('male', "Male"),
    ('female', "Female"),

)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    username = models.CharField(null=True, blank=True, max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    is_premium = models.BooleanField(default=False, blank=False)
    is_powers = models.BooleanField(default=False, blank=False)
    # Holds the user's bio
    bio = models.CharField(max_length=255, blank=True)
    # Holds the user's photo
    photo = models.ImageField(upload_to="users_profile_photo/", blank=True,
                              default="users_profile_photo/default_profile_photo.jpg")
    # Holds the user's date of birth
    date_of_birth = models.DateField(null=True, blank=False)
    # Holds the user's gender
    gender = models.CharField(choices=Gender, max_length=6)
    # Holds the location
    location = models.CharField(max_length=200)
    # Holds the user's phone number
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)

    def pic(self):
        return self.photo

    def __str__(self):
        return self.email

    def get_user_id(self):
        return reverse('account:show_profile', args=[self.pk])
