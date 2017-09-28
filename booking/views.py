from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Concert, Bookingoffer
from django.contrib.auth.decorators import login_required, user_passes_test
from .login_tests import (
    is_technician,
    is_booking_manager
)


# Create your views here.

@login_required()
def program_view(request):
    template_name = "booking/program.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


@user_passes_test(is_booking_manager)
def booking_view(request):
    template_name = "booking/booking.html"

    booking_offers = Bookingoffer.objects.all()
    booking_offers_count = booking_offers.count()
    print(booking_offers)
    print('boop')

    context = {
        'amount_booking_offers': booking_offers_count,
        

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


# I (auk) want to keep this test page for now as it (the template) contains solutions for not yet
# implemented functionality
def testuser(request):
    template_name = 'booking/testuser.html'

    concert_objs = Concert.objects.all()

    users_concerts = User.objects.get(username=request.user).concert_set.all()

    context = {
        'concerts': concert_objs,
        'users_concerts': users_concerts,
    }
    return render(request, template_name, context)
