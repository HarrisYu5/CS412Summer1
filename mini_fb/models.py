#File: mini_fb/models.py
#Author: Harris Yu 2025-06-03
#This file contains the models we use in the app, as well as the custom methods associated with them.

from django.db import models
from django.urls import reverse

#profile model
class Profile(models.Model):
    first_name = models.TextField(blank=True)
    last_name  = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profile_pic_url = models.TextField(blank=True)

    #override the __str__ method to return a string representation of the profile
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # return the URL to view the profil
    def get_absolute_url(self):
        return reverse("show_profile", kwargs={"pk": self.pk})
    #get all status messages for this profile
    def get_status_messages(self):
        return StatusMessage.objects.filter(profile=self)

#status message model
class StatusMessage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
#override the __str__ method to return a string representation of the status message
    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name} {self.message[:20]}"
    

class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(blank=True)


class StatusImage(models.Model):
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def get_images(self):
        return Image.objects.filter(status_message=self.status_message)
    
    

