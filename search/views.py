from django.shortcuts import render
from cards.models import Card
from decimal import Decimal, DecimalException


def basic_search(request):
    cards = Card.objects.filter(card_title__icontains=request.GET['search_title'])
    return render(request, 'cards.html', {'cards': cards})


def search_page(request):
    return render(request, 'search.html')


def advanced_search(request):
    min_price = request.GET['minprice']
    condition = request.GET['condition']
    decimal_min_price = Decimal(min_price)

    if decimal_min_price is None:
        new_price = 0.00
    else:
        new_price = decimal_min_price

    if condition == '1':
        cards = Card.objects.filter(
            card_title__icontains=request.GET['title'],
            card_edition__icontains=request.GET['edition'],
            user__username__icontains=request.GET['vendor'],
            card_price__gte=new_price)
        return render(request, 'cards.html', {'cards': cards})
    else:
        cards = Card.objects.filter(
            card_title__icontains=request.GET['title'],
            card_edition__icontains=request.GET['edition'],
            card_condition=request.GET['condition'],
            user__username__icontains=request.GET['vendor'],
            card_price__gte=new_price)
        return render(request, 'cards.html', {'cards': cards})
