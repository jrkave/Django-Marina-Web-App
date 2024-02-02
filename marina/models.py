from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Extending django.auth default User model 
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
    
class Boat(models.Model):
    boat_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.boat_name}, {self.type}, {self.owner}'

class BoatSpace(models.Model):
    availability_status = models.BooleanField(default=True)
    reserve_start = models.DateTimeField(null=True, blank=True)
    reserve_end = models.DateTimeField(null=True, blank=True)
    boat = models.ForeignKey(Boat, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("boatspace-detail", kwargs={"pk": self.pk})
    
    def clear_attributes(self):
        # Clear attributes when renting period ends
        self.availability_status = True
        self.reserve_start = None
        self.reserve_end = None
        self.boat = None
        self.save()

class BoatLicense(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_num = models.CharField(max_length=50)
    license_expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Boat License with number {self.license_num}"

