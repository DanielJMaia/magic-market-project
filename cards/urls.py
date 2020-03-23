from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from magicmarket.settings import MEDIA_ROOT
from .views import get_cards, get_card_details, create_or_edit_card


urlpatterns = [
    url(r'^$', get_cards, name='get_cards'),
]