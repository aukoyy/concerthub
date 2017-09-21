"""concerthub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Legg merke til at jeg har lagt til include på slutten i linjen under
from django.conf.urls import url, include
# Dette lar meg bruke urlpatterns fra andre filer enn bare denne

from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # I linjen under bruker jeg include til å inkludere urls fila fra appen jeg ønsker å inkludere
    url(r'^coolcats/', include('coolcats.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^lama/', include('lamatime.urls')),

    # Legg merke til at det ikke er noe $ tegn etter coolcats/
    # $ forteller browseren at url'en er slutt, og om den brukes her, vil ikke cats eller rocket
    # hentes, selv og man skriver coolcats/cats

]
