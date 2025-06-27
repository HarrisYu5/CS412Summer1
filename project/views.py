"""
File: views.py
Author: Harris Yu, hy002421@bu.edu, 2025-06-26
Description: Contains views for the project.
"""
from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime, timedelta
from django.utils import timezone


#home page: dashbord that shows current entries, total calories,

# Create your views here.

#simple view for welcome page
class WelcomeView(TemplateView):
    template_name = 'project/welcome.html'

#The main page, includes the dashboard that shows current entries and total calories, as well as the hisory of past 7 days
class MainPageView(LoginRequiredMixin, ListView):
    model = FoodEntry
    template_name = 'project/main.html'
    context_object_name = 'foodEntries'
    # get the food entries for the current day's daily entry
    def get_queryset(self):
        profile = self.request.user.profile

        today = timezone.localdate()
        #create or get the daily entry for today, ensure it exists
        daily_entry, created = DailyEntry.objects.get_or_create(
            user_profile=profile,
            date=today
        )

        self.daily_entry = daily_entry
        #print('daily_entry:', daily_entry) 

        return daily_entry.foodentry_set.all()
    
    #add context data to display on the main page. we display all the items in the current daily entry, and the past 7 daily entries
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_entry'] = self.daily_entry
        #print('daily_entry in context:', context)

        profile = self.request.user.profile
        today = timezone.localdate()
        yesterday = today - timedelta(days=1)
        past_week = today - timedelta(days=7)
        past = DailyEntry.objects.filter( #get past daily entries
            user_profile=profile,
            date__range=(past_week, yesterday)
        ).order_by('-date')
        context['past_entries'] = past
        #print('past_entries:', context['past_entries'])
        return context

#registration view
class RegistrationView(CreateView):
    template_name = 'project/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
#Simple detailview to display profile information
class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'project/profile.html'
    model = UserProfile
    context_object_name = 'userProfile'
#update profile information
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'project/update_profile.html'
    form_class = UpdateProfileForm
    model = UserProfile

    def form_valid(self, form):
            #print('updated:', form.cleaned_data)
            return super().form_valid(form)
    #get the success url, bring back to profile page
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
#create a food entry
class CreateFoodEntryView(LoginRequiredMixin, CreateView):
    template_name = 'project/create_food_entry.html'
    form_class = CreateFoodEntryForm
    #if there's no daily entry, create one
    def form_valid(self, form):
        profile = self.request.user.profile
        today = timezone.localdate()
        daily_entry, created = DailyEntry.objects.get_or_create(
            user_profile=profile,
            date=today
        )
        food_entry = form.save(commit=False)
        food_entry.daily_entry = daily_entry
        food_entry.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main')
#delete view for food entry, bring back the user to the main dashboard after deletion
class DeleteFoodEntryView(LoginRequiredMixin, DeleteView):
    context_object_name = 'foodEntry'
    template_name = 'project/delete_food_entry.html'
    model = FoodEntry

    def get_success_url(self):
        return reverse_lazy('main')
