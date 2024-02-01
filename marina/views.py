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
    # 'boatspace_list' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_list.html'
 
class BoatSpaceDetailView(generic.DetailView):
    # 'boatspace' is default context_object_name
    model = BoatSpace
    template_name = 'marina/boatspace_detail.html'
    


