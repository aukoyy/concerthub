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


class BookingOfferModelAdmin(admin.ModelAdmin):
    list_display = ['artist', 'updated_at', 'approved_by_bm', 'accepted_by_am']
    list_editable = ['approved_by_bm'] #Lar deg endre on the fly
    # list_display_links = ['updated_at'] #Styrer hva som er klikkbart
    list_filter = ['updated_at', 'booker'] #Man kan ha flere filtre
    search_fields = ['artist__name', 'comment', 'tech_needs'] #title og content er hva som er søkbart

    class Meta:
        model = BookingOffer


class ConcertModelAdmin(admin.ModelAdmin):
    list_display = ['artist', 'time_slot', 'tech_meetup_time', 'tech_done_time', 'created_at', 'updated_at']

    class Meta:
        model = Concert


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Concert, ConcertModelAdmin)
admin.site.register(Festival)
admin.site.register(Stage)
admin.site.register(BookingOffer, BookingOfferModelAdmin)
admin.site.register(TimeSlot)
