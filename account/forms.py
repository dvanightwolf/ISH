from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from .models import Profile
from datetime import datetime


class UserRegistrationForm(forms.ModelForm):
    """A class that represents a registration form for the Django User model."""
    # Holds the password
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    # A field to renter the password and match it with the entered password to make sure the password is what the
    # user meant it to be and they didn't make any typos
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        """A class to describe aspects of this model (self-referencing)."""
        # The model this form class represents
        model = User
        # The form's fields
        fields = ("username", "email")
        # Remove the username validation text
        help_texts = {"username": None}

    def clean_confirm_password(self):
        """Validates and makes sure that the 2 password fields match."""
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('confirm_password')

        # Do passwords match ?
        if password != password_confirm:
            # Raise an exception
            raise forms.ValidationError("Passwords don't match")

        if len(password) < 8 or len(password) > 16 and not any(char.isdigit() for char in password)\
                and not any(char for char in password):
            # Raise an exception
            raise forms.ValidationError("password should be at least 8 character and not be greater than 16 character"
                                        "and must contain at least one numeral and letter ")
        return cleaned_data


class ProfileForm(forms.ModelForm):
    """A class that represents a registration form for the Profile model."""
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1970, datetime.today().year + 1, 1)))

    class Meta:
        model = Profile
        fields = ("date_of_birth", "bio", "picture")


class UserEditForm(forms.ModelForm):
    """A class that represents a form to edit user's account."""
    class Meta:
        model = User
        fields = ("email", )


class ProfileEditForm(forms.ModelForm):
    """A class that represents a form to edit user's profile."""
    class Meta:
        model = Profile
        fields = ("bio", "picture")
