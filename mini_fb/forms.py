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