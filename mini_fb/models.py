from django.db import models

class Profile(models.Model):
    first_name = models.TextField(blank=True)
    last_name  = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profile_pic_url = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"