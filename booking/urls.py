from django.conf.urls import url
from .views import (
    program_view,
    booking_view,
    myconcerts,
    testuser,
)


urlpatterns = [
    url(r'^booking/$', booking_view, name='booking'),
    url(r'^program/$', program_view, name='program'),
    url(r'^myconcerts/$', myconcerts, name='myconcerts'),
    url(r'^testuser/$', testuser, name='testuser'),
]
