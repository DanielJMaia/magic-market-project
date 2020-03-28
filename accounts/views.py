from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, RegistrationForm
from cards.models import Card

def login(request):
    """
    This returns a login page
    """
    """login_form = UserLoginForm()"""
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home_page'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout(request):
    """
    logs out
    """
    cards = Card.objects.order_by('-listing_views')
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('home_page'))

def register(request):
    """
    registers a user
    """
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request),
                messages.success(request, "You have been successfully registered")
                return redirect('home_page')
            else:
                messages.error(request, "Unable to register your account, please try again later")
    else:            
        registration_form = RegistrationForm()
        
    return render(request, 'register.html', {
        "registration_form": registration_form})