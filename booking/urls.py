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
    BookingUpdateArtistManager,
    BookingUpdateBooker,
    accept_booking,
    decline_booking,
    UpdateArtistReview,
    TechMeetupUpdate,
    concert_reports_view,
    pr_man_view,
)


urlpatterns = [
    url(r'^program/$', program_view, name='program'),
    url(r'^organizer_overview/$', organizer_view, name='organizer_view'),
    url(r'^booking_overview/$', booking_manager_view, name='booking_manager_view'),
    url(r'^accept_booking/$', accept_booking, name='accept_booking'),
    url(r'^decline_booking/$', decline_booking, name='decline_booking'),
    url(r'^booking/$', booker_view, name='booker_view'),
    url(r'^work_hours/$', technician_view, name='technician_view'),
    url(r'^festival_info/$', pr_man_view, name='festival_info'),
    url(r'^offers_concerts/$', artist_manager_view, name='artist_manager_view'),
    url(r'^concert_reports/$', concert_reports_view, name='concert_reports_view'),
    url(r'^offers_concerts/(?P<pk>\w+)/update/$', BookingUpdateArtistManager.as_view()),
    url(r'^booking/(?P<pk>\w+)/update/$', BookingUpdateBooker.as_view()),
    url(r'^booking/(?P<pk>\w+)/delete/$', BookingDelete.as_view()),
    url(r'new$', BookingCreate.as_view(), name='bookingoffer_new'),
    url(r'^artist/(?P<pk>\w+)/update/$', UpdateArtistReview.as_view()),
    url(r'^work_hours/(?P<pk>\w+)/update/$', TechMeetupUpdate.as_view()),
]
