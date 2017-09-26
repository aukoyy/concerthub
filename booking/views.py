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

def myconcerts(request):
    template_name = "booking/myconcerts.html"

    myconcert_objs = Concert.objects.all()

    context = {
        'myconcerts': myconcert_objs,
    }

    return render(request, template_name, context)
