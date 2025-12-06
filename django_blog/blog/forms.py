from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post


# Form for creating a new user

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Profile Form

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


# Profile Update Form

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic"]


# Form for Post Model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]