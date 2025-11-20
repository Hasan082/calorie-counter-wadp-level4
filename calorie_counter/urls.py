from django.urls import path
from.views import (
    user_registration,
    login_view,
    dashboard_view,
    ProfileView,
    CalorieEntryView
)


urlpatterns = [
    path('register/', user_registration, name='register'),
    path('', login_view, name='login'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('profile/', ProfileView, name='profile'),
    path('calorie-entry/', CalorieEntryView, name='calorie_entry'), # type: ignore
]
