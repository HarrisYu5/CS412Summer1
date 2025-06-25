from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Food)
admin.site.register(UserProfile)
admin.site.register(DailyEntry)
admin.site.register(FoodEntry)
