from django.db import models
# Required Imports for makeing the custom user model
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField

#+++++++++++++++++ ACCOUNT MANAGER ++++++++++++++++++++
class Account_Manager(BaseUserManager):
    # Creating User
    def create_user(self,email,password = None):
        user = self.model(
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    # Creating Super User
    def create_superuser(self,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
    

#+++++++++++++++++++++++ USER'S ACCOUNT +++++++++++++++++++++++
class Account(AbstractBaseUser,PermissionsMixin): # Inorder to use this custom model we have to set this in 'settings.py' as "AUTH_USER_MODEL = 'users.Account'"
    username = models.CharField(max_length = 10,blank = True,null =True) # Username will not be used for take username,it's the field present by default so can't be replaced but can be ignored and left empty
    email = models.EmailField(max_length = 200,blank = False,null =False,unique = True) # Email will be our priority and making it as unique 
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    
    USERNAME_FIELD = "email" # Setting the username field to take email
    
    objects = Account_Manager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
 #+++++++++++++++++++ USER'S MORE INFO FOR THEIR ACCOUNT +++++++++++++++++++++++++   
class Account_more_info(models.Model): # User's can add more info about once the account is created from their profile
    phone_no = models.CharField(max_length = 10,blank = True,null =True)
    author = models.ForeignKey(Account,default = None,on_delete = models.CASCADE) # Inheriting the Model 'Account' as the author 


 #++++++++++++++++ Event Section +++++++++++++++++++++++++

class Event(models.Model):
    event_poster = CloudinaryField("Event Posters", resource_type="image", blank=True, null=True)
    event_type = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

class EventDetails(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='event_details')
    summary = models.TextField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    social_media_links = models.JSONField(blank=True, null=True)
    location = models.CharField(max_length=255)
    event_poster = CloudinaryField("Event Posters", resource_type="image", blank=True, null=True)

    def __str__(self):
        return f"Details for {self.event.event_name}"
    

class EventPicture(models.Model):
    image = CloudinaryField("Images", resource_type="image")
    author = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.event_name} - Picture"

    class Meta:
        verbose_name_plural = "Event Pictures"


    
    
