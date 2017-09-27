from django.shortcuts import render
from django.contrib.auth.models import User, Group
import platform
import django

from django.contrib.auth.decorators import login_required, user_passes_test

# For å kunne bruke models, altså tabellene i databasen vår, må de importeres
from .models import LaunchPlatform



def is_cat(user):
    return True

@login_required(login_url='/login/')
def dont(request):
    template_name = 'coolcats/lookat.html'

    python_version = platform.python_version()
    django_version = django.get_version()

    # user = User.objects.get(username="org1")
    # user_member_of = user.groups.all()

    context = {
        'python_version': python_version,
        'django_version': django_version,
        # 'user_member_of': user_member_of,
    }

    return render(request, template_name, context)





# Her begynner det å bli synlig hvorfor det var så kult å kunne sende stuff til templates i context:
@user_passes_test(is_cat)
def rocket(request):
    template_name = 'coolcats/rockets.html'

    # Dette er en query som henter alle objektene i launchplatform inkludert evt. koblinger.
    # Ettersom modellen LaunchPlatform har både Manufacturer og Engine som Foreignkey, kan man
    # akksessere begge igjennom kun LaunchPlatform.
    launchPlatforms = LaunchPlatform.objects.all()

    context = {
        'launchers': launchPlatforms,
    }

    return render(request, template_name, context)