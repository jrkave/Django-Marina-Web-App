from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Extending User model using 1-1 link
class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    has_valid_license = models.BooleanField(default=False)
    has_valid_insurance = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        """String for representing UserProfile object"""
        return self.username
    
    def get_absolute_url(self):
        """Returns URL to access particular instance of the model"""
        # TO DO: URL mapping, view, template 
        return reverse("model_detail", kwargs={"pk": self.pk})

class Boat(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.type}, {self.owner}'

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

class BoatSpace(models.Model):
    availability_status = models.BooleanField(default=True)
    reserve_start = models.DateTimeField(null=True, blank=True)
    reserve_end = models.DateTimeField(null=True, blank=True)
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
