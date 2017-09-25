from django.conf.urls import url
from .views import basic_lama

urlpatterns = [
    url(r'^hi/$', basic_lama, name="lama"),
]
