from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Concert
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

@login_required()
def booking(request):
    template_name = "booking/firstpage.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


@login_required()
def myconcerts(request):
    template_name = "booking/myconcerts.html"

    # Following query requests model Stages through the current user object, and thus
    # only fetches the stages that have the current user registered under technicians
    myconcert_objs = User.objects.get(username=request.user).concert_set.all()

    context = {
        'myconcerts': myconcert_objs,
    }

    return render(request, template_name, context)


@login_required()
def technical(request):
    template_name = 'booking/technical.html'
    return render(request, template_name, {})


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
