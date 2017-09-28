from django.conf.urls import url
from .views import (
    booking,
    technician_view,
    testuser,
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^technician/$', technician_view, name='technician_view'),
    url(r'^testuser/$', testuser, name='testuser'),
]
