from django.shortcuts import render
from cards.models import Card


def basic_search(request):
    cards = Card.objects.filter(card_title__icontains=request.GET['search_title'])
    return render(request, 'cards.html', {'cards': cards})


def search_page(request):
    return render(request, 'search.html')


def advanced_search(request):
    condition = request.GET['condition']
    if condition == '1':
        cards = Card.objects.filter(
            card_title__icontains=request.GET['title'],
            card_edition__icontains=request.GET['edition'],
            user__username__icontains=request.GET['vendor'])
        return render(request, 'cards.html', {'cards': cards})
    else:
        cards = Card.objects.filter(
            card_title__icontains=request.GET['title'],
            card_edition__icontains=request.GET['edition'],
            card_condition=request.GET['condition'],
            user__username__icontains=request.GET['vendor'])
        return render(request, 'cards.html', {'cards': cards})
