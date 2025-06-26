from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


#home page: dashbord that shows current entries, total calories,

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'project/base.html'

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