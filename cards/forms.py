from django import forms
from .models import Card

class = CardDescForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'content', 'image', 'tag', 'published_date')