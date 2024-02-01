from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Boat, BoatSpace, BoatLicense, BoatRegistration

# Register your models here.

@admin.register(CustomUser) # Decorator provides same functionality as .register() syntax
class CustomUserAdmin(admin.ModelAdmin):
    """Changes how the model is displayed in admin interface"""
    list_display = ('username', 'email', 'phone_number')

@admin.register(Boat) 
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner')

@admin.register(BoatSpace)
class BoatSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'availability_status', 'reserve_start', 'reserve_end', 'boat')

@admin.register(BoatLicense)
class BoatLicenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_num', 'license_expiry_date')
    
@admin.register(BoatRegistration)
class BoatRegistrationAdmin(admin.ModelAdmin):
    list_display = ('hull_id', 'boat')

# admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Boat)
# admin.site.register(BoatSpace)