from django import forms
from .models import Card

class CardDescForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('card_title', 'card_description', 'card_edition', 'card_condition', 'card_price', 'image', 'listing_published_date')