from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import timedelta
from .models import CustomUser, Boat, BoatSpace, PhoneNumberField, BoatLicense

# Create your forms here. 
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'phone_number']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Use ModelForms (over forms.Form) since this has a corresponding model
class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = ['boat_name', 'type', 'owner']

class BoatSpaceForm(forms.ModelForm):
    class Meta:
        model = BoatSpace
        fields = ['reserve_start', 'boat']
        
    def save(self, commit=True):
        boatspace = super().save(commit=False)
        
        # Set more attributes and save
        boatspace.availability_status = False
        boatspace.reserve_end = boatspace.reserve_start + timedelta(days=14)
        
        if commit:
            boatspace.save()
            
        return boatspace

class BoatLicenseForm(forms.ModelForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    
    class Meta:
        model = BoatLicense
        fields = ['license_num', 'license_expiry_date']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Check if a CustomUser with the provided username and email exists
        try:
            custom_user = CustomUser.objects.get(username=username, email=email)
        except CustomUser.DoesNotExist:
            raise ValidationError("Invalid username or email")
