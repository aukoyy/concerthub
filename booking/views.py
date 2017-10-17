from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import UpdateView

from .models import (
    Concert,
    BookingOffer,
    TimeSlot,
    Artist,
)
from .login_tests import (
    is_technician,
    is_booking_manager,
    is_artist_manager,
    is_booker,
    is_organizer,
    is_booking_manager_or_organizer,
)


def program_view(request):
    template_name = "booking/program.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


@user_passes_test(is_organizer)
def organizer_view(request):
    template_name = "booking/organizer.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


@user_passes_test(is_booking_manager_or_organizer)
def booking_manager_view(request):
    template_name = "booking/booking_manager.html"

    booking_offers = BookingOffer.objects.all()
    booking_offers_count = booking_offers.count()
    booked_slots = []
    available_slots = []

    for obj in TimeSlot.objects.all():
        if not hasattr(obj, "concert"):
            available_slots.append(obj)
        elif hasattr(obj, 'concert'):
            booked_slots.append(obj)

    context = {
        'amount_booking_offers': booking_offers_count,
        'available_slots': available_slots,
        'booking_offers': booking_offers,
        'booked_slots': booked_slots,
    }

    return render(request, template_name, context)


@user_passes_test(is_booker)
def booker_view(request):
    template_name = 'booking/booker.html'

    bookingoffer_objs = User.objects.get(username=request.user).booker.all()

    context = {
        'bookingoffers': bookingoffer_objs,
    }
    return render(request, template_name, context)


@user_passes_test(is_technician)
def technician_view(request):
    template_name = "booking/technician.html"

    concert_objs_for_user = User.objects.get(username=request.user).concert_set.all()

    context = {
        'concert_objs': concert_objs_for_user,
    }

    return render(request, template_name, context)


@user_passes_test(is_artist_manager)
def artist_manager_view(request):
    template_name = "booking/artist_manager.html"

    # artist_objs = User.objects.get(username=request.user).artist.all()
    # TODO: Filter offers by username of artist_manager
    # bookingoffer_objs = BookingOffer.objects.all()
    bookingoffer_objs = User.objects.get(username=request.user).bookingoffer_set.all()
    # BookingOffer.objects.filter(artist_manager__name__icontains='auk')  # get(concert_manager=request.user)

    context = {
        # 'artists': artist_objs,
        'bookingoffers': bookingoffer_objs,
    }
    return render(request, template_name, context)


class BookingUpdate(UpdateView):
    model = BookingOffer
    fields = [
        'tech_needs',
        'accepted_by_am',
    ]
    template_name = 'booking/bookingmodel_update_form.html'
    # template_name_suffix = '_update_form'
    success_url = '/booking/offers_concerts'
