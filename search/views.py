from django.shortcuts import render
from cards.models import Card


def do_search(request):
    cards = Card.objects.filter(card_title__icontains=request.GET['q'])
    return render(request, 'cards.html', {'cards': cards})
