from django.shortcuts import render
from django.views.generic import ListView



# Create your views here.

class placeholder_view(ListView):
    template_name = 'placeholder.html'