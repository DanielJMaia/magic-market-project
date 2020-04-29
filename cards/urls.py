from django.conf.urls import url
from .views import home_page, get_cards, get_card_details, create_or_edit_card, view_specific_card

urlpatterns = [
    url(r'^$', home_page, name='home_page'),
    url(r'^cards/$', get_cards, name='get_cards'),
    url(r'^(?P<pk>\d+)/$', get_card_details, name='card_detail'),
    url(r'^new/$', create_or_edit_card, name="new_card"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_card, name="edit_card"),
    url(r'^cards/(?P<pk>\d+)$', view_specific_card, name='view_specific_card'),
    
]
