from django.contrib import admin
from .models import (
    Genre,
    Artist,
    Concert,
    Festival,
    Stage,
    BookingOffer,
    TimeSlot,
)

# Register your models here.

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Festival)
admin.site.register(Stage)
admin.site.register(BookingOffer)
admin.site.register(TimeSlot)
