from django.shortcuts import render


def dont(request):
    template_name = 'coolcats/lookat.html'

    import platform
    pythonVersion = platform.python_version()
    import django
    djangoVersion = django.get_version()

    context = {
        'python_version': pythonVersion,
        'django_version': djangoVersion,
    }

    return render(request, template_name, context)




from .models import Manufacturer, LaunchPlatform

def rocket(request):
    template_name = 'coolcats/rockets.html'

    launchPlatforms = LaunchPlatform.objects.all()

    context = {
        'launchers': launchPlatforms,
    }

    return render(request, template_name, context)