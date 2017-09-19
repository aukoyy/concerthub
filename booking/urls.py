
# Dette er en fil for å ha kun urlpatterns tilhørende denne appen (coolcats)

from django.conf.urls import url


# Bruk følgende syntaks for å importere funksjoner ifra views
# Det går også an å importere hele views in one blow og skrive views.dont og views.rocket
# lenger nede. For hver gang dere gjør det, dreper jeg en kul katt. Ikke gjør det >:{
from .views import (
    booking,

)


# Legg merke til linjen "url(r'^coolcats/', include('coolcats.urls'))," i prosjektets urls.py
# Der har vi allerede registrert coolcats/ som url. Dvs. at det vi registrer her kommer i tillegg.
# Ønsker vi den første i browseren skriver vi /coolcats/cats. De legger seg altså etter hverandre
urlpatterns = [
    url(r'^firstpage/$', booking),

    # Her brukes $ for å markere slutten på url'en. I motsetning til i prosjektets urls.py
]