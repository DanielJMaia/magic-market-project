from django.conf.urls import url
from .views import login, logout, register, view_user, view_profile

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),
    url(r'^user/$', view_user, name="view_user"),
    url(r'^profile/(?P<pk>\d+)/$', view_profile, name="view_profile"),
]
