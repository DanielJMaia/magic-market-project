from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Card
from .forms import CardDescForm


def home_page(request):
    cards = Card.objects.order_by('-listing_views')
    return render(request, 'home.html', {'cards': cards})


def get_cards(request):
    """
    Create a view that will return a list of cards that have been
    uploaded to the website by users
    """
    card_list = Card.objects.all()

    """
    for card in cards:
        print(card.user)
    """

    page = request.GET.get('page', 1)

    paginator = Paginator(card_list, 20)
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)

    return render(request, "cards.html", {'cards': cards})


def view_specific_card(request, pk):
    """
    This view allows the user to click on a specific card name and view all
    listings of the same name
    """
    card_id = get_object_or_404(Card, pk=pk)
    card_name = card_id.card_title
    cards = Card.objects.filter(card_title__icontains=card_name)
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

