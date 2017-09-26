from django.conf.urls import url
from .views import (
    booking,
    myconcerts,
)


urlpatterns = [
    url(r'^firstpage/$', booking, name='booking'),
    url(r'^myconcerts/$', myconcerts, name='myconcerts'),
]
