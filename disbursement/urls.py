from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_management, name='user_management'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/add/', views.device_create, name='device_create'),
    path('devices/edit/<int:device_id>/', views.edit_device, name='edit_device'),
    path('devices/delete/<int:device_id>/', views.delete_device, name='delete_device'),
    path('devices/<int:device_id>/add-specification/', views.add_specification, name='add_specification'),
    path('specifications/edit/<int:spec_id>/', views.edit_specification, name='edit_specification'),
    path('specifications/delete/<int:spec_id>/', views.delete_specification, name='delete_specification'),
    path('devices/import-export/', views.import_export_devices, name='import_export_devices'),
    path('roles/', views.role_list, name='role_list'),
    path('roles/add/', views.add_role, name='add_role'),
    path('roles/edit/<int:role_id>/', views.edit_role, name='edit_role'),
    path('roles/delete/<int:role_id>/', views.delete_role, name='delete_role'),
    path('user-roles/', views.user_role_list, name='user_role_list'),
    path('user-roles/delete/<int:user_role_id>/', views.delete_user_role, name='delete_user_role'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('', include('django_prometheus.urls')),
]