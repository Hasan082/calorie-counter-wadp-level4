from django.shortcuts import render, redirect   
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import ProfileForm,CalorieEntryForm
from django.contrib.auth.decorators import login_required
from .models import Profile, CalorieConsumed


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfull! Login Now")
            return redirect("login")
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form,
        'login_flag': True
    }
    return render(request, 'login.html', context)



def dashboard_view(request):
    caloriedata = CalorieConsumed.objects.filter(user=request.user)
    profile_data = Profile.objects.get(user=request.user)
    bmr = profile_data.bmr
    context={
        'caloriedata': caloriedata,
        'caloure_consumed': caloriedata.order_by('-date').first(),
        'req_bmr': round(bmr, 2) # type: ignore
    }
    return render(request, 'dashboard.html', context)


@login_required
def ProfileView(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.calculate_bmr()
            messages.success(request, "Profile info Updated successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Any fio the form filed is invalid")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
        
    context = {
        'form' : form,
        'profile_form': True
    }

    return render(request, "profile.html", context)



def CalorieEntryView(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, "Profile info Updated successfully")
            return redirect("dashboard")
        else:
            messages.error(request, 'Form data is invalid')
    else:
        form = CalorieEntryForm()
        
    context = {
        'form' : form,
    }

    return render(request, "calorie.html", context)
    
    
    