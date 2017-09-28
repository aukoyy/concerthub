from django.conf.urls import url
from .views import (
    program_view,
    booking_view,
    technician_view,
    testuser,
)


urlpatterns = [
    url(r'^booking/$', booking_view, name='booking'),
    url(r'^program/$', program_view, name='program'),
    url(r'^technician/$', technician_view, name='technician_view'),
    url(r'^testuser/$', testuser, name='testuser'),
]
