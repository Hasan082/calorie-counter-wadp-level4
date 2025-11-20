from django.urls import path
from.views import (
    user_registration,
    login_view,
    dashboard_view,
    ProfileView,
    ProfileUpdateView,
    CalorieEntryView
)


urlpatterns = [
    path('register/', user_registration, name='register'),
    path('', login_view, name='login'),
    path('dashboard', dashboard_view, name='dashboard'),
    
    # path('calorie-entry/', CalorieEntryView, name='calorie-entry'),
    
    # path('profile/', ProfileView, name='profile'),
    # path('profile-update/', ProfileUpdateView, name='profile'),
]
