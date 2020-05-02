from django.conf.urls import url
from .views import login, logout, register, view_user, view_profile, view_all_user_cards, view_history

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),
    url(r'^user/$', view_user, name="view_user"),
    url(r'^user/history/$', view_history, name="view_history"),
    url(r'^profile/(?P<pk>\d+)/$', view_profile, name="view_profile"),
    url(r'^(?P<pk>\d+)/all/$', view_all_user_cards, name="view_all_user_cards"),
]
