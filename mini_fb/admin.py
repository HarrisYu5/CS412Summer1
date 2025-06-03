from django.contrib import admin

# Register your models here.

from .models import Profile, StatusMessage

#register models we use in the app
admin.site.register(Profile)
admin.site.register(StatusMessage)