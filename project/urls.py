from django.urls import path
from .views import  *

urlpatterns = [
    path('', placeholder_view.as_view(), name='placeholder_view'),
]
