from django.conf.urls import url
from .views import get_cards

urlpatterns = [
    url(r'^$', get_cards, name='get_cards'),
]