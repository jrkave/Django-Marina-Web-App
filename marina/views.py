from django.shortcuts import render
from django.views import generic

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

# Generic views
class BoatSpaceListView(generic.ListView):
    model = BoatSpace
    context_object_name = 'boatspace_list' # name for list as template variable

class BoatSpaceDetailView(generic.DetailView):
    model = BoatSpace
    


