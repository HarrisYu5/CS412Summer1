"""
File: forms.py
Author: Harris Yu, hy002421@bu.edu, 2025-06-26
Description: Contains forms for user registration, profile updates, and food entry creation.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *

# Registration form for new users
class RegistrationForm(UserCreationForm):
    sex = forms.ChoiceField(choices=UserProfile.sex_choices, required=True)
    age = forms.IntegerField(required=True)
    height = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
    # Override the save method to create the user profile, it creates a new UserProfile instance and save it.
    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = UserProfile(
            user=user,
            sex=self.cleaned_data['sex'],
            age=self.cleaned_data['age'],
            height=self.cleaned_data['height'],
            weight=self.cleaned_data['weight']
        )
        profile.save()
        return user
#Form for update profile information
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'weight', 'height', 'override_calories_goal', 'sex']
#form for creating a food entry
class CreateFoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['food', 'number_of_servings']


