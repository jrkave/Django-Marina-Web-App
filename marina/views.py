from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from datetime import datetime, time

from .forms import SignupForm, LoginForm, BoatLicenseForm, BoatForm, BoatSpaceForm
from .models import BoatSpace

# Create your views here.
def index(request):
    """View function for home page"""
    return render(request, 'marina/index.html')

from django.shortcuts import render
from .models import BoatSpace

def profile(request):
    user = request.user

    # Filter boatspaces based on the user's username
    user_boatspaces = BoatSpace.objects.filter(boat__owner=user)

    # Pass the user_boatspaces to the template context
    context = {'user_boatspaces': user_boatspaces}
    return render(request, 'marina/profile.html', context)

def success(request):
    return render(request, 'marina/success.html')

# Signup Page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'marina/signup.html', {'form': form, 'form_css': 'marina/css/forms.css'})

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
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'marina/login.html', {'form': form, 'form_css': 'marina/css/forms.css'})

# Logout Page
def user_logout(request):
    logout(request)
    return redirect('index')

# Register a BoatLicense 
def submit_license(request):
    user = request.user
    if request.method == 'POST':
        form = BoatLicenseForm(request.POST)
        if form.is_valid():
            license_registration = form.save(commit=False)
            license_registration.user = request.user
            license_registration.save()
            user.set_valid_license()
            return redirect('success')
    else:
        form = BoatLicenseForm()
    return render(request, 'marina/license.html', {'form': form, 'form_css': 'marina/css/forms.css',})

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
    return render(request, 'marina/add_boat.html', {'form': form, 'form_css': 'marina/css/forms.css',})

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
    return render(request, 'marina/register_boatspace.html', {'form': form, 'form_css': 'marina/css/forms.css',})

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

    return render(request, 'marina/edit_boatspace.html', {'form': form, 'form_css': 'marina/css/forms.css', 'boatspace': boatspace})

class BoatSpaceListView(generic.ListView):
    model = BoatSpace
    template_name = 'marina/boatspace_list.html'
    
    def get_context_data(self, **kwargs):
        # Get specific context for template (see func below)
        context = super().get_context_data(**kwargs)
        context['available_boats_count'] = self.get_available_boats_count()
        return context

    def get_available_boats_count(self):
        # Retrieve the count of available boatspaces
        return BoatSpace.objects.filter(availability_status=True).count()