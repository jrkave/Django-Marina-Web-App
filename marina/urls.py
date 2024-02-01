from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('boatspaces/', views.BoatSpaceListView.as_view(), name='boatspace-list'),
    path('boatspaces/<int:pk>/', views.BoatSpaceDetailView.as_view(), name='boatspace-detail'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('success', views.success, name='success'),
]
