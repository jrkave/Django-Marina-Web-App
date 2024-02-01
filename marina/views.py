from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import UserCreationForm, SignupForm, LoginForm
from .models import BoatSpace

# Create your views here.
def index(request):
    """View function for home page"""
    return render(request, 'marina/index.html')

def auth(request):
    return render(request, 'marina/auth.html')

def reservations(request):
    return render(request, 'marina/reservations.html')

def profile(request):
    return render(request, 'marina/profile.html')

def success(request):
    return render(request, 'marina/success.html')

# Signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SignupForm()
    return render(request, 'marina/signup.html', {'form': form})

# Login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('success')
    else:
        form = LoginForm()
    return render(request, 'marina/login.html', {'form': form})

# Logout Page
def user_logout(request):
    logout(request)
    return redirect('success')

# Generic views
class BoatSpaceListView(generic.ListView):
    # 'boatspace_list' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_list.html'
 
class BoatSpaceDetailView(generic.DetailView):
    # 'boatspace' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_detail.html'
    


