#File: mini_fb/forms.py
#Author: Harris Yu 2025-06-03
#This file contains the forms we use in the app
from django import forms
from .models import Profile, StatusMessage

#form for creating a profile
class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'profile_pic_url']

#form for creating a status message, profile and timestap are set in the view
class CreateStatusMessageForm(forms.ModelForm):

    class Meta:
        model = StatusMessage
        fields = ['message']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'email', 'profile_pic_url']

class UpdateStatusMessageForm(forms.ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['message']