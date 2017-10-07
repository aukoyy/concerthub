from django.conf.urls import url
from .views import (
    booker_view,
    program_view,
    booking_manager_view,
    technician_view,
    artist_manager_view
)


urlpatterns = [
    url(r'^program/$', program_view, name='program'),  # For organizer first but open to all logged in
    url(r'^booking_overview/$', booking_manager_view, name='booking_manager_view'),
    url(r'^booking/$', booker_view, name='booker_view'),
    url(r'^work_hours/$', technician_view, name='technician_view'),
    url(r'^offers_concerts/$', artist_manager_view, name='artist_manager_view'),
]
