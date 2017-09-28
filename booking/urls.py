from django.conf.urls import url
from .views import (
    booking,
    myconcerts,
    testuser,
    artist_manager_view
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^myconcerts/$', myconcerts, name='myconcerts'),
    url(r'^testuser/$', testuser, name='testuser'),
    url(r'^artist_manager/$', artist_manager_view, name='artist_manager'),
]
