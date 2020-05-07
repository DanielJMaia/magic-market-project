from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, RegistrationForm
from cards.models import Card
from checkout.models import Order, OrderLineItem


def login(request):
    """
    This returns a login page
    """
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
                return redirect('/')
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout(request):
    """
    logs out
    """
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect('/')


def register(request):
    """
    registers a user
    """
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have been successfully registered")
                return render(request, 'user_profile.html', {"profile": user})
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = RegistrationForm()
    return render(request, 'register.html', {
        "registration_form": RegistrationForm})


@login_required
def view_user(request):
    """This retrieves the user from the database and redirects to their profile page"""
    user = User.objects.get(email=request.user.email)
    cards = Card.objects.filter(~Q(card_amount__icontains=0), user=user)
    return render(request, 'user_profile.html', {"profile": user, "cards": cards})


def view_all_user_cards(request, pk):
    """This shows the all cards table, filtered to only show the user's cards"""
    profile = get_object_or_404(User, pk=pk)
    card_list = Card.objects.filter(~Q(card_amount__icontains=0), user=profile)

    page = request.GET.get('page', 1)

    paginator = Paginator(card_list, 20)
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)

    return render(request, 'cards.html', {"profile": profile, "cards": cards})


def view_profile(request, pk):
    """This allows users to view vendor profiles by retrieving the vendor id and redirecting it to their profile page"""
    profile = get_object_or_404(User, pk=pk)
    cards = Card.objects.filter(~Q(card_amount__icontains=0), user=profile)
    return render(request, 'user_profile.html', {"profile": profile, "cards": cards})


@login_required
def view_history(request):
    user = User.objects.get(email=request.user.email)
    order_list = Order.objects.filter(user=user).order_by("id").reverse()
    order_line = OrderLineItem.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(order_list, 3)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request, 'order_history.html', {"user": user, "orders": orders, "order_line": order_line})
