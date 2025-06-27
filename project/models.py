"""
File: models.py
Author: Harris Yu, hy002421@bu.edu, 2025-06-26
Description: Contains models needed for this app, as well as custom methods
"""
from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
#The food methods, This include all the food user can choose from to add to their daily entry
class Food(models.Model):
    name = models.TextField(blank=False, max_length=200)
    serving_size = models.TextField(blank=True)
    calories_per_serving = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.serving_size}, {self.calories_per_serving}"
    #hard coded load data method, use publically available data from kaggle
    def load_data():
        path = r"C:\Users\Salmon\Desktop\CS412Summer1\data\nutrients_csvfile.csv"
        f  = open(path)
        f.readline() # skip header

        for line in f:
            fields = line.split(',')
            #for each line in the csv, we create a new Food instance
            try:
                food = Food(name = fields[0],
                            serving_size = fields[1],
                            calories_per_serving = int(fields[3]))
                food.save()
                print(f"Saved food: {food}")
            except :
                print(f"Error processing line: {line}." )
        print("Finished loading data.")

# User profile model, contains the user's information, and use that information to dynamically calculate the calories needed
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
    override_calories_goal = models.IntegerField(blank=True, null=True) #can be left blank
    height = models.FloatField(blank=True, null=True) 
    weight = models.FloatField(blank=True, null=True) 
    age = models.IntegerField(blank=True, null=True) 

    def calories_goal(self): # Calculate the user's calorie goal, if there's a override, use that
        if self.override_calories_goal:
            return self.override_calories_goal
        else:
            return self.auto_calories_goal()
    
    def auto_calories_goal(self): 
    # Mifflin-St Jeor Equation: 
    #source: https://www.calculator.net/calorie-calculator.html?cage=25&csex=m&cheightfeet=5&cheightinch=10&cpound=165&cheightmeter=180&ckg=65&cactivity=1.465&cmop=0&coutunit=c&cformula=m&cfatpct=20&printit=0&ctype=metric
        W = self.weight
        H= self.height
        A = self.age

        if self.sex == 'M':
            bmr = 10 * W + 6.25 * H - 5 * A + 5
        elif self.sex == 'F':
            bmr = 10 * W + 6.25 * H - 5 * A - 161
        elif self.sex == 'O':
            bmr_male = 10 * W + 6.25 * H - 5 * A + 5
            bmr_female = 10 * W + 6.25 * H - 5 * A - 161
            bmr = (bmr_male + bmr_female) / 2
        else:
            bmr = 10 * W + 6.25 * H - 5 * A  

        return int(bmr)




    def __str__(self):
        return f"{self.user.username}, {self.user.email}"
# Daily entry model, contains the food entries for a specific day for a specific
class DailyEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #date = models.DateField(auto_now_add=True)
    date = models.DateField(default=date.today)

    
    class Meta:
        unique_together = ('user_profile', 'date')

    def __str__(self):
        return f"{self.user_profile.user.username}, {self.date} entry"
    #get the sum of the calories for that daily entry
    def total_calories(self):
        total = 0
        for entry in self.foodentry_set.all():
            total += entry.food.calories_per_serving * entry.number_of_servings

        return total
    #calculate how much calories the user has left for the day, negative means over the limit already
    def remaining_calories(self):
        return self.user_profile.calories_goal() - self.total_calories()
# Food entry model, contains the food entries for a specific day for a specific user,
class FoodEntry(models.Model):
    daily_entry = models.ForeignKey(DailyEntry, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    number_of_servings = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.daily_entry.user_profile.user.username} {self.food.name}, {self.number_of_servings} servings"
    
    def calories(self):
        return self.food.calories_per_serving * self.number_of_servings