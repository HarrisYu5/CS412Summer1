#File: mini_fb/admin.py
#Author: Harris Yu 2025-06-03
#This file registers the models we use in the app
from django.contrib import admin

# Register your models here.

from .models import *

#register models we use in the app
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)
admin.site.register(StatusImage)
admin.site.register(Friend)

