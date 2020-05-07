from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth, messages
from django.db.models import Q
from django.http import HttpResponseForbidden, HttpResponse
from .models import Card
from .forms import CardDescForm


def home_page(request):
    cards = Card.objects.filter(~Q(card_amount__icontains=0))
    return render(request, 'home.html', {'cards': cards})


def get_cards(request):
    """
    Create a view that will return a list of cards that have been
    uploaded to the website by users
    """
    cards = Card.objects.filter(~Q(card_amount__icontains=0))
    return render(request, "cards.html", {'cards': cards})


def view_specific_card(request, pk):
    """
    This view allows the user to click on a specific card name and view all
    listings of the same name
    """
    card_id = get_object_or_404(Card, pk=pk)
    card_name = card_id.card_title
    cards = Card.objects.filter(~Q(card_amount__icontains=0), card_title__icontains=card_name)
    return render(request, "cards.html", {'cards': cards})


def get_card_details(request, pk):
    """
    Returns a single card object and renders
    it on the cardinformation.html template
    """
    card = get_object_or_404(Card, pk=pk)
    card.listing_views += 1
    card.save()
    return render(request, "cardinformation.html", {'card': card})


def create_or_edit_card(request, pk=None):
    """
    This allows us to create or edit a post
    """
    card = get_object_or_404(Card, pk=pk) if pk else None
    if request.method == "POST":
        form = CardDescForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card = form.save()
            return redirect(get_card_details, card.pk)
    else:
        form = CardDescForm(instance=card)
    return render(request, 'addcards.html', {'form': form})


def delete_listing(request, pk):
    """
    This deletes a card after showing a warning message
    """
    card = get_object_or_404(Card, pk=pk)
    if (request.user.is_authenticated):
        try:
            card.delete()
            messages.success(request, "You've successfully deleted the listing")
        except Card.DoesNotExist:
            messages.warning(request, 'This listing could not be deleted. Please try again later.')
    else:
        return HttpResponseForbidden()
    return redirect('/')
