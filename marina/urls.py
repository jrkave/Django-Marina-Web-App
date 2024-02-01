from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authentication/', views.auth, name='authentication'),
    path('reservations/', views.reservations, name='reservations'),
    path('profile/', views.profile, name='profile'),
    path('boatspaces/', views.BoatSpaceListView.as_view(), name='boatspaces'),
    path('boatspaces/<int:pk>/', views.BoatSpaceDetailView.as_view(), name='boatspace-detail')
    
]
