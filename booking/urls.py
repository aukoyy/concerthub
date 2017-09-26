from django.conf.urls import url
from .views import (
    booking,
)

urlpatterns = [
    url(r'^firstpage/$', booking),
]

