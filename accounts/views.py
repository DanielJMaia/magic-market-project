from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm

def logout(request):
    """
    logs out
    """
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('home_page'))

def login(request):
    """
    This returns a login page
    """
    login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})