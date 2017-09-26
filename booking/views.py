from django.shortcuts import render
from .models import Concert

# Create your views here.


def booking(request):
    template_name = "booking/firstpage.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)


from django.contrib.auth.models import User

def testuser(request):
    template_name = 'booking/testuser.html'

    concert_objs = Concert.objects.all()

    users_concerts = User.objects.get(username=request.user).concert_set.all()


    context = {
        'concerts': concert_objs,
        'users_concerts': users_concerts,
    }

    return render(request, template_name, context)
