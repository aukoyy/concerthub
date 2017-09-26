from django.conf.urls import url
from .views import (
    booking,
    myconcerts,
    testuser,
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^myconcerts/$', myconcerts, name='myconcerts'),
    url(r'^testuser/$', testuser, name='testuser'),
]
