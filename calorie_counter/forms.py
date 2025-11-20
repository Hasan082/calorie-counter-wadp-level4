from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CalorieConsumed, Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class CalorieEntryForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    item_name = forms.CharField(max_length=200)
    calorie_consumed = forms.IntegerField(min_value=0)
    
    class Meta:
        model = CalorieConsumed
        fields = ['date', 'item_name', 'calorie_consumed']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'gender', 'age', 'weight', 'height']
        
        
