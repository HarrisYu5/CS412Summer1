#File: mini_fb/urls.py
#Author: Harris Yu 2025-06-03
# This file contains the URL patterns for the mini_fb app

from django.urls import path
from .views import  *

urlpatterns = [

    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('profile/create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status/', CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/delete/', DeleteStatusMessageView.as_view(), name='delete_status_message'),
    path('status/<int:pk>/update/', UpdateStatusMessageView.as_view(), name='update_status_message'),

]
