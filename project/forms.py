from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    sex = forms.ChoiceField(choices=UserProfile.sex_choices, required=True)
    age = forms.IntegerField(required=True)
    height = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
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

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'weight', 'height', 'override_calories_goal', 'sex']

        

