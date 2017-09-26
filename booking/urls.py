from django.conf.urls import url
from .views import (
    booking,
    testuser,
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^testuser/$', testuser, name='booking2'),
]
