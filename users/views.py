from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import Profile, Contact
from .forms import ProfileUpdateForm, ContactForm

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    
    context = {
        'registerform': form
    }
    return render(request, "register.html", context)  
  
def login(request):
    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'loginform': form}
    return render(request, "login.html", context)   

def logout(request):
    auth.logout(request)
    return redirect("login") 

def my_profile(request):
    profile = request.user.profile  # Преземете го тековниот профил
    if request.method == 'POST':
        print("POST data received:", request.POST)  # Дебагирање: Примени податоци
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print("Form is valid. Saving data...")
            form.save()
            print("Profile saved successfully!")
            return redirect('my_profile')  # Пренасочување по зачувувањето
        else:
            print("Form is not valid:", form.errors)  # Дебагирање: Грешки во формата
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    
    return render(request, 'my_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('password')
        new_password = request.POST.get('newpassword')
        re_new_password = request.POST.get('renewpassword')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return redirect('my_profile')

        if new_password != re_new_password:
            messages.error(request, "New passwords do not match.")
            return redirect('my_profile')

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)

        messages.success(request, "Your password has been updated successfully.")
        return redirect('my_profile')
    return redirect('my_profile')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("POST data received:", request.POST)  # Debugging
        if form.is_valid():
            print("Form is valid")  # Debugging
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request, "There was an error. Please try again.")
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)

@login_required
def all_contacts(request):
    messages = Contact.objects.all().order_by('-created_at')  # Сите пораки, сортирани од најновите
    return render(request, 'all_contacts.html', {'messages': messages})

