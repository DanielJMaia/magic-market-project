from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Card
from .models import CardDescForm

def get_cards(request):
    """
    Create a view that will return a list of cards that have been
    uploaded to the website by users
    """
    cards = Card.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "cardlist.html", {'cards': cards})

def get_card_info(request):
    """
    Create a view that returns a single card object
    based on the ID and render it on carddetail.html.
    Return 404 if not found.
    """
    card = get_object_or_404(Card, pk=pk)
    card.views += 1
    card.save()
    return render(request, "cardinfo.html", {'card': card})

def create_or_edit_cards(request, pk=None):
    """
    Create a view that allows us to create or edit a card
    based on ID
    """
    card = get_object_or_404(Card, pk=pk) if pk else None
    if request.method == "POST":
        card = CardDescForm(request.POST, request.FILES, instance=card)
        if card.is_valid():
            card = form.save()
            return redirect(get_card_info, card.pk)
    else:
        form = CardDescForm(instance=card)
    return render(request, 'carddescform.html'), {'card': card}