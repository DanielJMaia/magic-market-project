from django.conf.urls import url
from .views import basic_search, search_page, advanced_search


urlpatterns = [
    url(r'^$', basic_search, name='search'),
    url(r'^search', search_page, name='search_page'),
    url(r'^advanced$', advanced_search, name='advanced_search'),
]
