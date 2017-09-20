from django.conf.urls import url
from .views import basic_lama

urlpatterns = [
    url(r'^lama/$', basic_lama()),
]

