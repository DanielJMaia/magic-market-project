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

def get_card_details(request, pk):
    """
    Returns a single card object and renders
    it on the cardinformation.html template
    """
    card = get_object_or_404(Card, pk=pk)
    card.views += 1
    card.save()
    return render(request, "cardinformation.html", {'card': card})

def create_or_edit_card(request, pk=None):
    """
    This allows us to create or edit a post
    """
    card = get_object_or_404(Card, pk=pk) if pk else None
    if request.method == "POST":
        card = CardDescForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save()
            return redirect(card_detail, card.pk)
    else:
        card = CardDescForm(instance=card)
    return render(request, 'addcards.html', {'form': form})