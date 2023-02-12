from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth import login
from django.http import HttpResponse


def register(request):
    """Handles user registration to the website."""
    # Is it a post request ?
    if request.method == "POST":
        # Instantiate a UserCreationForm and ProfileForm with the submitted data
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        # The data are valid ?
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but don't save it to the database just yet
            new_user = user_form.save(commit=False)
            # Set the provided password as this registration's password
            new_user.set_password(user_form.cleaned_data["password"])
            # Since we got a password for this registration save it to the database
            new_user.save()
            # Create a profile that corresponds to this user with and set the given birthday and bio
            profile = Profile.objects.create(user=new_user,
                                             date_of_birth=profile_form.cleaned_data["date_of_birth"],
                                             bio=profile_form.cleaned_data["bio"])
            # Did the user submit a profile picture?
            # If so set it as their picture otherwise it's blank ("gonna add a default pic later)
            if request.FILES:
                profile.picture = profile_form.files["picture"]
            # Save the profile in case more data were provided
            profile.save()
            # Log the user in
            login(request, new_user)
            # A dictionary that holds the data to be sent to the corresponding html page
            context = {"new_user": new_user, "profile_form": profile_form}
            # Everything went well render send the user to the registration success page
            return render(request, "temp_home.html", context)

    # Not a POST request
    else:
        # Instantiate an empty instance of both UserCreationForm and ProfileForm
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    # A dictionary that holds the data to be sent to the corresponding html page
    context = {"user_form": user_form, "profile_form": profile_form}
    # Registration wasn't successful for some reason so render the registration page with empty forms
    return render(request, "registration/register.html", context)


def user_profile(request):
    """A view to display the user's profile."""
    user = request.user
    # Get the user's profile
    profile = user.profile
    # Send it over to the HTMl for render
    context = {"profile": profile, "user": user}
    # Render the requested page
    return render(request, "profile/user_profile.html", context)


def profile_edit(request):
    """A view to edit user's profile."""
    # Get the user's profile
    profile = request.user.profile
    # Is it a POST request by the account's owner ?
    if request.method == "POST":
        # Instantiate a UserEditForm and ProfileEditForm with the submitted data
        user_edit_form = UserEditForm(request.POST, instance=request.user)
        profile_to_edit_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        # Are both forms valid ?
        if profile_to_edit_form.is_valid() and user_edit_form.is_valid():
            # Save the user
            user_edit_form.save()
            # Did the user submit a profile picture?
            # If so set it as their new picture
            if request.FILES:
                profile.picture = profile_to_edit_form.files["picture"]
            # User doesn't want to update their profile picture rather they want to remove it?
            # Set the default picture as their profile
            elif not request.FILES and not profile.picture:
                profile.picture = "users_profile_pic/default_profile_pic.jpg"
            # Save the profile
            profile.save()
            return HttpResponse("Profile was updated successfully")
    # Not a post request
    else:
        # Instantiate a UserEditForm and ProfileEditForm with original data
        user_edit_form = UserEditForm(instance=request.user)
        profile_to_edit_form = ProfileEditForm(instance=profile)
    context = {"user_edit_form": user_edit_form, "profile_to_edit": profile_to_edit_form}
    return render(request, "profile/edit.html", context)
