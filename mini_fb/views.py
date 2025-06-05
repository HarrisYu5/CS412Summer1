#File: mini_fb/views.py
#Author: Harris Yu 2025-06-03
#This file contains the views we use in the app

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
import datetime
from django.urls import reverse
from .forms import *





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
        form.instance.profile = Profile.objects.get(pk=pk)
        form.instance.timestamp = datetime.datetime.now()

        response = super().form_valid(form)

        for file in self.request.FILES.getlist('files'):
            image = Image.objects.create(profile=form.instance.profile, image_file=file)
            image.save()
            statusMessage = StatusImage.objects.create(status_message=form.instance, image=image)
            statusMessage.save()
        return response

# Redirect to the profile page after creating a status message
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    

class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class DeleteStatusMessageView(DeleteView):
    template_name = 'mini_fb/delete_status_form.html'
    model = StatusMessage
    context_object_name = 'status_message'


    def get_success_url(self):
        profile = self.object.profile
        return reverse('show_profile', kwargs={'pk': profile.pk})


class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    