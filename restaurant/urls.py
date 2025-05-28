from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'), 
    path('main',views.main, name='main'),
    path('order',views.order, name='order'),
    path('confirm',views.confirm, name='confirm'),
    
 ]