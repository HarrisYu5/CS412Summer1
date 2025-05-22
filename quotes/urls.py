from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'), 
    path('quote/', views.home, name='quote'),
    path('show_all/', views.show_all, name='show_all'),
    path('about/', views.about, name='about'), 
 ]
 