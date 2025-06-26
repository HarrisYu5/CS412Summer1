from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.VoterListView.as_view(), name='voters'),
]