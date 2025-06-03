from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
import datetime
from django.urls import reverse





# Create your views here.

#show all profile
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html' 
    context_object_name = 'profiles'

#show a single profile, with more details and the ability to see and create status messages
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'
#create a profile with a form
class CreateProfileView(CreateView):
    model = Profile
    template_name = 'mini_fb/create_profile_form.html'
    fields = ['first_name', 'last_name', 'city', 'email', 'profile_pic_url']

    def form_valid(self, form):
        return super().form_valid(form)
    
#create a status message for a profile with a form
class CreateStatusMessageView(CreateView):
    model = StatusMessage
    template_name = 'mini_fb/create_status_form.html'
    fields = ['message']

#set the profile and timestamp in the form before saving
    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        profile = Profile.objects.get(pk=pk)

        form.instance.profile = profile

        form.instance.timestamp = datetime.datetime.now()

        return super().form_valid(form)
# Redirect to the profile page after creating a status message
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    

