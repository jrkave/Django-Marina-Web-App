from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser, PhoneNumberField

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