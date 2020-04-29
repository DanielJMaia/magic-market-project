from django.conf.urls import url
from .views import basic_search, search_page, advanced_search


urlpatterns = [
    url(r'^$', basic_search, name='search'),
    url(r'^advanced/$', search_page, name='search_page'),
    url(r'^advanced/results/$', advanced_search, name='advanced_search'),
]
