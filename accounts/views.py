from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm

def login(request):
    """
    This returns a login page
    """
    """login_form = UserLoginForm()"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout(request):
    """
    logs out
    """
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('home_page'))
