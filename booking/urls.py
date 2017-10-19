from django.conf.urls import url
from .views import (
    booker_view,
    program_view,
    booking_manager_view,
    technician_view,
    artist_manager_view,
    organizer_view,
    BookingCreate,
    BookingDelete,
    BookingUpdate_for_artist_manager,
    BookingUpdate_for_booker,
)


urlpatterns = [
    url(r'^program/$', program_view, name='program'),

    url(r'^organizer_overview/$', organizer_view, name='organizer_view'),
    url(r'^booking_overview/$', booking_manager_view, name='booking_manager_view'),
    url(r'^booking/$', booker_view, name='booker_view'),
    url(r'^work_hours/$', technician_view, name='technician_view'),
    url(r'^offers_concerts/$', artist_manager_view, name='artist_manager_view'),

    url(r'^offers_concerts/(?P<pk>\w+)/update/$', BookingUpdate_for_artist_manager.as_view()),

    url(r'^booking/(?P<pk>\w+)/update/$', BookingUpdate_for_booker.as_view()),
    url(r'^booking/(?P<pk>\w+)/delete/$', BookingDelete.as_view()),
    url(r'new$', BookingCreate.as_view(), name='bookingoffer_new'),
]
