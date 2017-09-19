from django.contrib import admin

# Register your models here.


# For å kunne se modellene sine i /admin, må de registreres her
# Imorter og registrer slik som under og sjekk at de dukker opp i /admin
from .models import (
    Manufacturer,
    LaunchPlatform,
    GitMemes,
    Engine,
)

# Disse må registreres en og en. Putter man mer inn som parametre, oppfattes
# det av django som ytteligere argumenter da det er mulig
admin.site.register(Manufacturer)
admin.site.register(LaunchPlatform)
admin.site.register(Engine)
admin.site.register(GitMemes)