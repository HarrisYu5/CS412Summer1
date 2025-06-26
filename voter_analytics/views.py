from django.shortcuts import render
from django.views.generic import ListView
from .models import Voter


class VoterListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voter_list.html'
    context_object_name = 'voters'
    ordering = ['voter_score']
    paginate_by = 100

    