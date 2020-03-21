from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Card
from .forms import CardDescForm

def get_cards(request):
    """
    Create a view that will return a list of cards that have been
    uploaded to the website by users
    """
    cards = Card.objects.filter(listing_published_date__lte=timezone.now())
    return render(request, "cards.html", {'cards': cards})