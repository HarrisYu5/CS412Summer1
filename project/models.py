from django.db import models
from django.conf import settings

# Create your models here.
class Food(models.Model):
    name = models.TextField(blank=False, max_length=200)
    serving_size = models.TextField(blank=True)
    calories_per_serving = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.serving_size}, {self.calories_per_serving}"
    
    def load_data():
        path = r"C:\Users\Salmon\Desktop\CS412Summer1\data\nutrients_csvfile.csv"
        f  = open(path)
        f.readline() # skip header

        for line in f:
            fields = line.split(',')

            try:
                food = Food(name = fields[0],
                            serving_size = fields[1],
                            calories_per_serving = int(fields[3]))
                food.save()
                print(f"Saved food: {food}")
            except :
                print(f"Error processing line: {line}." )
        print("Finished loading data.")


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

    def calories_goal(self):
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

class DailyEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    
    class Meta:
        unique_together = ('user_profile', 'date')

    def __str__(self):
        return f"{self.user_profile.user.username}, {self.date} entry"

    def total_calories(self):

        total = 0

        for entry in self.foodentry_set.all():
            total += entry.food.calories_per_serving * entry.number_of_servings

        return total
    def remaining_calories(self):
        return self.user_profile.calories_goal() - self.total_calories()

class FoodEntry(models.Model):
    daily_entry = models.ForeignKey(DailyEntry, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    number_of_servings = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.daily_entry.user_profile.user.username} {self.food.name}, {self.number_of_servings} servings"
    
    def calories(self):
        return self.food.calories_per_serving * self.number_of_servings