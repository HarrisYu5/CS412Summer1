from django.db import models
from django.conf import settings

# Create your models here.
class Food(models.Model):
    name = models.TextField(blank=True)
    serving_size = models.TextField(blank=True)
    calories_per_serving = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.serving_size}, {self.calories_per_serving}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    sex_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = models.CharField(max_length=1, choices=sex_choices, blank=True)
    override_calories_goal = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True) 
    weight = models.FloatField(blank=True, null=True) 
    age = models.IntegerField(blank=True, null=True) 



    def __str__(self):
        return f"{self.user.username}, {self.user.email}"

class DailyEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username}, {self.date} entry"

class FoodEntry(models.Model):
    daily_entry = models.ForeignKey(DailyEntry, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    number_of_servings = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.daily_entry.user_profile.user.username} {self.food.name}, {self.number_of_servings} servings"
    