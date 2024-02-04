from django.db import models
# Required Imports for makeing the custom user model
from django.conf import settings
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField


 #++++++++++++++++ Event Section +++++++++++++++++++++++++

class Event(models.Model):
    poster = CloudinaryField("Event Posters", resource_type = "image", blank = False, null = False)
    name = models.CharField(max_length = 200,blank = False, null = False)
    type = models.CharField(max_length = 100,blank = False, null = False)
    starting_date = models.DateTimeField(blank = False, null = False)
    ending_date = models.DateTimeField(blank = False, null = False)
    published = models.BooleanField(default = False,blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class EventDetails(models.Model):
    summary = models.TextField(blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 500,blank = True, null = True)
    location = models.TextField(blank = True, null = True)
    author = models.OneToOneField(Event, on_delete = models.CASCADE, related_name = 'event_details')
    event_poster = CloudinaryField("Event Posters", resource_type="image", blank=True, null=True)

    def __str__(self):
        return f"Details for {self.event.event_name}"
    

class EventPicture(models.Model):
    image = CloudinaryField("Images", resource_type="image")
    author = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "event_pictures")


# Event Social media handels
class EventSNS(models.Model):
    instagram = models.TextField(blank = True,null = True)
    facebook = models.TextField(blank = True,null = True)
    twitter = models.TextField(blank = True,null = True)
    youtube = models.TextField(blank = True,null = True)
    website = models.TextField(blank = True,null = True)
    author = models.OneToOneField(Event, on_delete = models.CASCADE, related_name = 'event_social_media')
   



    
    



    
    
