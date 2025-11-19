from django.contrib import admin
from .models import Profile, CalorieConsumed

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'weight', 'height')
    
   
@admin.register(CalorieConsumed)   
class CalorieConsumedAdmin(admin.ModelAdmin):
    list_display = ('date', 'item_name', 'calorie_consumed')
