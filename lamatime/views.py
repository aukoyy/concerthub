from django.shortcuts import render
import platform
import django
import random


def basic_lama(request):
    template_name = 'lama/basic.html'
    rand = random.randint(0, 8)
    lama_names = ['South', 'South-West', 'West', 'North-West', 'North', 'North-East', 'East', 'South-East']

    python_version = platform.python_version()
    django_version = django.get_version()

    context = {
        'python_version': python_version,
        'django_version': django_version,
        'lama_name': lama_names[rand],
    }

    return render(request, template_name, context)


