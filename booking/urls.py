from django.conf.urls import url
from .views import (
    booker_view,
    program_view,
    booking_manager_view,
    technician_view,
    artist_manager_view,
    organizer_view,

    BookingCreate,
    BookingUpdateArtistManager,
    BookingUpdateBooker,
    BookingDelete,

    accept_booking,
    decline_booking,


    TimeSlotCreate,
    TimeSlotUpdate,
    TimeSlotDelete,
    UpdateArtistReview,
    TechMeetupUpdate,
    concert_reports_view,
    pr_man_view,
)


urlpatterns = [
    # general program view and organizer_view
    url(r'^program/$', program_view, name='program'),
    url(r'^organizer_overview/$', organizer_view, name='organizer_view'),

    # booker view and BookingOffer logic
    url(r'^booking/$', booker_view, name='booker_view'),
    url(r'^new$', BookingCreate.as_view(), name='bookingoffer_new'),
    url(r'^booking/(?P<pk>\w+)/update/$', BookingUpdateBooker.as_view()),
    url(r'^booking/(?P<pk>\w+)/delete/$', BookingDelete.as_view()),

    # booking_manager view, TimeSlot logic and accept/decline logic for BookingOffer
    url(r'^booking_overview/$', booking_manager_view, name='booking_manager_view'),
    url(r'^booking_overview/create/$', TimeSlotCreate.as_view(), name='timeslot_create'),
    url(r'^booking_overview/(?P<pk>\w+)/update/$', TimeSlotUpdate.as_view()),
    url(r'^booking_overview/(?P<pk>\w+)/delete/$', TimeSlotDelete.as_view()),
    url(r'^accept_booking/$', accept_booking, name='accept_booking'),
    url(r'^decline_booking/$', decline_booking, name='decline_booking'),

    # technician view and meetup logic
    url(r'^work_hours/$', technician_view, name='technician_view'),
    url(r'^work_hours/(?P<pk>\w+)/update/$', TechMeetupUpdate.as_view()),

    # artist_manager view, limited BookingOffer and Artist logic
    url(r'^offers_concerts/$', artist_manager_view, name='artist_manager_view'),
    url(r'^concert_reports/$', concert_reports_view, name='concert_reports_view'),
    url(r'^artist/(?P<pk>\w+)/update/$', UpdateArtistReview.as_view()),
    url(r'^offers_concerts/(?P<pk>\w+)/update/$', BookingUpdateArtistManager.as_view()),

    # pr_man view
    url(r'^festival_info/$', pr_man_view, name='pr_man_view'),

]
