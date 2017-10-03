from django.conf.urls import url
from .views import (
    booker_view,
    booking,
    technician_view,
    testuser,
    artist_manager_view
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^technician/$', technician_view, name='technician_view'),
    url(r'^testuser/$', testuser, name='testuser'),
    url(r'^booker/$', booker_view, name='booker'),
    url(r'^artist_manager/$', artist_manager_view, name='artist_manager'),
]
