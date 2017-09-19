from django.shortcuts import render

# Create your views here.

from .models import Concert
def booking(request):
    template_name = "booking/firstpage.html"

    objs = Concert.objects.all()

    context = {
        'concerts': objs,
    }

    return render(request, template_name, context)




