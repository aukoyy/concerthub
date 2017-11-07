from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotFound


from .models import (
    Concert,
    BookingOffer,
    TimeSlot,
    Artist,
    Stage,
)

from .login_tests import (
    is_technician,
    is_artist_manager,
    is_booker,
    is_organizer,
    is_booking_manager_or_organizer,
    is_pr_man,
)

from .forms import TimeSlotForm


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


@user_passes_test(is_pr_man)
def pr_man_view(request):
    template_name = "booking/pr_man.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


@user_passes_test(is_booking_manager_or_organizer)
def concert_reports_view(request):
    template_name = "booking/concert_reports.html"

    stage = Stage.objects.all()
    timeslot = TimeSlot.objects.all()
    concert = Concert.objects.all()

    stage_dict = dict()

    for t in timeslot:
        for c in concert:
            if t.stage not in stage_dict and c.time_slot == t:
                stage_dict[t.stage] = [c]
            elif t.stage in stage_dict and c.time_slot == t:
                stage_dict[t.stage].append(c)

    context = {
        'stages': stage,
        'timeslots': timeslot,
        'concerts': concert,
        'stage_dict': stage_dict,
    }

    return render(request, template_name, context)


@user_passes_test(is_booking_manager_or_organizer)
def booking_manager_view(request):
    template_name = "booking/booking_manager.html"

    booking_offers = BookingOffer.objects.all()
    booking_offers_count = booking_offers.count()
    booked_slots = []
    available_slots = []

    stages = Stage.objects.all()
    time_slot_form = TimeSlotForm(request.POST or None)
    if time_slot_form.is_valid():
        instance = time_slot_form.save(commit=False)
        instance.save()

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
        'time_slot_form': time_slot_form,
        'stages': stages,
    }

    if request.method == "POST":
        print(request.POST.get("start_date"))
        print(request.POST.get("end_time"))

    return render(request, template_name, context)


@user_passes_test(is_booker)
def booker_view(request):
    template_name = 'booking/booker.html'

    booking_offer_objs = User.objects.get(username=request.user).booker.all()
    print(booking_offer_objs[0].artist.artist_rev)
    distinct_offers = []
    for offer in booking_offer_objs:
        if offer.artist not in distinct_offers:
            distinct_offers.append(offer.artist)

    context = {
        'bookingoffers': booking_offer_objs,
        'distinct_offers': distinct_offers,
    }
    return render(request, template_name, context)


def accept_booking(request):
    if request.method == 'POST':
        offer_id = request.POST.get('offer', None)
        offer = get_object_or_404(BookingOffer, pk=offer_id)
        offer.approved_by_bm = True
        offer.save()
        return redirect('booking_manager_view')


def decline_booking(request):
    if request.method == 'POST':
        offer_id = request.POST.get('offer', None)
        print(offer_id)
        offer = get_object_or_404(BookingOffer, pk=offer_id)
        offer.approved_by_bm = False
        offer.save()
        return redirect('booking_manager_view')


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

    concert_objs = Concert.objects.filter(artist__artist_manager=request.user)
    bookingoffer_objs = BookingOffer.objects.filter(artist__artist_manager=request.user)

    context = {
        'bookingoffers': bookingoffer_objs,
        'concerts': concert_objs,
    }
    return render(request, template_name, context)


class TimeSlotCreate(CreateView):
    model = TimeSlot
    template_name = 'booking/model_create_form.html'
    form_class = TimeSlotForm

    success_url = '/booking/booking_overview'


class TimeSlotUpdate(UpdateView):
    model = TimeSlot
    template_name = 'booking/model_update_form.html'
    form_class = TimeSlotForm

    success_url = '/booking/booking_overview'


class TimeSlotDelete(DeleteView):
    model = TimeSlot
    template_name = 'booking/model_delete_form.html'
    success_url = '/booking/booking_overview'


class BookingCreate(CreateView):
    model = BookingOffer
    template_name = 'booking/model_create_form.html'

    fields = [
        'artist',
        'artist_manager',
        'comment',
        'time_slot',
        'price',
        'tech_needs',
        'booker',
    ]
    success_url = '/booking/booking'


class BookingDelete(DeleteView):
    model = BookingOffer

    template_name = 'booking/model_delete_form.html'
    success_url = '/booking/booking'


class BookingUpdateArtistManager(UpdateView):
    model = BookingOffer
    template_name = 'booking/model_update_form.html'

    fields = [
        'tech_needs',
        'accepted_by_am',
    ]

    success_url = '/booking/offers_concerts'


class BookingUpdateBooker(UpdateView):
    model = BookingOffer
    template_name = 'booking/model_update_form.html'

    fields = [
        'artist',
        'comment',
        'time_slot',
        'price',
        'tech_needs',
        'booker',
    ]
    success_url = '/booking/booking'


class UpdateArtistReview(UpdateView):
    model = Artist
    template_name = 'booking/model_update_form.html'

    fields = [
        'artist_rev',
    ]
    success_url = '/booking/booking_overview'


class UpdateBookerArtistReview(UpdateView):
    model = Artist
    template_name = 'booking/model_update_form.html'

    fields = [
        'artist_rev',
    ]
    success_url = '/booking/booking'


class TechMeetupUpdate(UpdateView):
    model = Concert
    template_name = 'booking/model_update_form.html'
    fields = {'techs_met'}
    success_url = '/booking/work_hours'
