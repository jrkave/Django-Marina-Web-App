from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, LoginForm, BoatLicenseForm, BoatRegistrationForm, BoatForm, BoatSpaceForm
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

# Signup Page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SignupForm()
    return render(request, 'marina/signup.html', {'form': form})

# Login Page
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

# Register a BoatLicense 
def submit_license(request):
    if request.method == 'POST':
        form = BoatLicenseForm(request.POST)
        if form.is_valid():
            license_registration = form.save(commit=False)
            license_registration.user = request.user
            license_registration.save()
            return redirect('success')
    else:
        form = BoatLicenseForm()
    return render(request, 'marina/license.html', {'form': form})

# Register a BoatRegistration
def submit_registration(request):
    if request.method == 'POST':
        form = BoatRegistrationForm(request.POST)
        if form.is_valid():
            boat_registration = form.save(commit=False)
            boat_registration.user = request.user  # Associate the registration with the currently-logged-in user
            boat_registration.save()
            return redirect('success')
    else:
        form = BoatRegistrationForm()
    return render(request, 'marina/registration.html', {'form': form})

# Register a Boat
def register_boat(request):
    if request.method == 'POST':
        form = BoatForm(request.POST)
        if form.is_valid():
            boat = form.save(commit=False)
            boat.save()
            return redirect('success')
    else:
        form = BoatForm()
    return render(request, 'marina/add_boat.html', {'form': form})

# Register a BoatSpace 
def register_boatspace(request):
    if request.method == 'POST':
        form = BoatSpaceForm(request.POST)
        if form.is_valid():
            boatspace = form.save(commit=False)
            boatspace.save()
            return redirect('success')
    else:
        form = BoatSpaceForm()
    return render(request, 'marina/register_boatspace.html', {'form': form})

# Edit a BoatSpace
def edit_boatspace(request, boatspace_id):
    # Retrieve the BoatSpace instance
    boatspace = get_object_or_404(BoatSpace, pk=boatspace_id)

    if request.method == 'POST':
        # Populate the form with the existing data and update it with the submitted data
        form = BoatSpaceForm(request.POST, instance=boatspace)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        # Populate the form with the existing data for display
        form = BoatSpaceForm(instance=boatspace)

    return render(request, 'marina/edit_boatspace.html', {'form': form, 'boatspace': boatspace})

# Generic views
class BoatSpaceListView(generic.ListView):
    # 'boatspace_list' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_list.html'
 
class BoatSpaceDetailView(generic.DetailView):
    # 'boatspace' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_detail.html'
    


