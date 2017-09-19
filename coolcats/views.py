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



# For å kunne bruke models, altså tabellene i databasen vår, må de importeres
from .models import LaunchPlatform

# Her begynner det å bli synlig hvorfor det var så kult å kunne sende stuff til templates i context:
def rocket(request):
    template_name = 'coolcats/rockets.html'

    # Dette er en query som henter alle objektene i launchplatform inkludert evt. koblinger.
    # Ettersom modellen LaunchPlatform har både Manufacturer og Engine som Foreignkey, kan man
    # akkessere begge igjennom kun LaunchPlatform.
    launchPlatforms = LaunchPlatform.objects.all()

    context = {
        'launchers': launchPlatforms,
    }

    return render(request, template_name, context)