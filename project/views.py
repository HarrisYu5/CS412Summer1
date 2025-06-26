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


class WelcomeView(TemplateView):
    template_name = 'project/welcome.html'

class MainPageView(LoginRequiredMixin, ListView):
    model = FoodEntry
    template_name = 'project/main.html'
    context_object_name = 'foodEntries'

    def get_queryset(self):
        profile = self.request.user.profile

        today = timezone.localdate()
        daily_entry, created = DailyEntry.objects.get_or_create(
            user_profile=profile,
            date=today
        )

        self.daily_entry = daily_entry
        print('daily_entry:', daily_entry)

        return daily_entry.foodentry_set.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_entry'] = self.daily_entry
        print('daily_entry in context:', context)
        return context
         

class RegistrationView(CreateView):
    template_name = 'project/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'project/profile.html'
    model = UserProfile
    context_object_name = 'userProfile'

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'project/update_profile.html'
    form_class = UpdateProfileForm
    model = UserProfile

    def form_valid(self, form):
            print('updated:', form.cleaned_data)
            return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
    
class CreateFoodEntryView(LoginRequiredMixin, CreateView):
    template_name = 'project/create_food_entry.html'
    form_class = CreateFoodEntryForm
    
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
    
class DeleteFoodEntryView(LoginRequiredMixin, DeleteView):
    context_object_name = 'foodEntry'
    template_name = 'project/delete_food_entry.html'
    model = FoodEntry

    def get_success_url(self):
        return reverse_lazy('main')
