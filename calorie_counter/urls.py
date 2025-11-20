from django.urls import path
from django.contrib.auth.views import LogoutView
from.views import (
    user_registration,
    login_view,
    dashboard_view,
    ProfileView,
    CalorieEntryView
)


urlpatterns = [
# Authentication
    path('auth/register/', user_registration, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    
    # Main pages
    path('', dashboard_view, name='dashboard'),
    path('profile/', ProfileView, name='profile'),
    path('calorie/entry/', CalorieEntryView, name='calorie_entry'),
]
