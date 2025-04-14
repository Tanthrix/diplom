from django.contrib import admin
from .models import CustomUser, Role, UserRole, Device, Specification, Room

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name']
    search_fields = ['username', 'full_name']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'get_role_name_display']
    search_fields = ['role_name']

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user__username', 'role__role_name']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'status', 'room', 'added_by']
    search_fields = ['name', 'serial_number']

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['device', 'name', 'value']
    search_fields = ['name', 'value']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number']
    search_fields = ['number']