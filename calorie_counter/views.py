from django.shortcuts import render, redirect   
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import ProfileForm,CalorieEntryForm
from django.contrib.auth.decorators import login_required
from .models import Profile, CalorieConsumed
from django.utils import timezone
from django.db.models import Sum
from django.db.utils import OperationalError



def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfull! Login Now")
            return redirect("login")
        else:
            messages.error(request, "Registration Failed! Invalid Information")
            return redirect("register")
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login Successfull!")
            profile , created = Profile.objects.get_or_create(user=request.user)
            if created:
                messages.warning(request, "Update your profile please!")
            return redirect('dashboard')
        else:
            messages.error(request, "Login Failed! Invalid Credentials")
            return redirect("login")
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
        'login_flag': True
    }
    return render(request, 'login.html', context)


@login_required
def dashboard_view(request):
    # Try to order by date (newest first) and then by creation time so latest added appears first.
    # If migrations adding `created_at` haven't been applied yet, fall back to ordering by date only.
    try:
        caloriedata = CalorieConsumed.objects.filter(user=request.user).order_by('-date', '-created_at')
        # force a small DB hit to ensure the `created_at` column exists
        caloriedata.exists()
    except OperationalError:
        caloriedata = CalorieConsumed.objects.filter(user=request.user).order_by('-date')
    today = timezone.localdate()
    try:
        total_calories_today = caloriedata.filter(date=today).aggregate(total=Sum('calorie_consumed'))['total'] or 0
    except Exception:
        total_calories_today = 0

    profile_data, created = Profile.objects.get_or_create(user=request.user or None)
    bmr = profile_data.bmr if profile_data.bmr else 0
    context={
        'caloriedata': caloriedata,
        'total_cal': total_calories_today,
        'req_bmr': round(bmr, 2) # type: ignore
    }
    return render(request, 'dashboard.html', context)


@login_required
def ProfileView(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if created:
        messages.warning(request, "Update your profile first")
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.calculate_bmr()
            messages.success(request, "Profile info Updated successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Any of the form filed is invalid")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
        
    context = {
        'form' : form,
        'profile_form': True
    }

    return render(request, "profile.html", context)


@login_required
def CalorieEntryView(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, "Calorie info Updated successfully")
            return redirect("dashboard")
        else:
            messages.error(request, 'Form data is invalid')
            return redirect("calorie_entry")
    else:
        form = CalorieEntryForm()
        
    context = {
        'form' : form,
    }

    return render(request, "calorie.html", context)
    
    
    