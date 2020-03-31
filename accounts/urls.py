from django.conf.urls import url
from .views import login, logout, register, view_user

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),
    url(r'^profile/$', view_user, name="view_user")
]
