from django.db import models


# Her har jeg laget litt eksempellsnadder som kan brukes til referanse når vi
# utvikler andre deler av prosjektet.

# Ta en titt på conserthub.herokuapp.com/coolcats/rockets for å se dette i praksis med litt data
# Om jeg har kommet så langt. + /admin vil kunne gi en del innsikt. bruk: - pass: -

# Dette er filen som brukes for å sette opp database-tabeller. En modell, f.eks. Engine vil ved hjelp av
# djangos migrering bli til en tabell i postgres databasen vår. Linjenene under migreres til felter i tabellen.
# Her har jeg altså opprettet tre tabeller med noen felter hver seg.

# Det er i forbindelse med modellering at det er viktig å migrere: makemigrations/migrate
# Hver eneste gang noe endres i denne filen, kjør de kommandoene. Det er noen unntak, men det skader aldri.

class Manufacturer(models.Model):
    # CharField er et tekstinput
    name = models.CharField(max_length=120)
    # TextField er et stort tekstinput.
    # null=True, blank=True er parametre som gjør at man ikke MÅ fylle ut feltet.
    description = models.TextField(null=True, blank=True)


    # Dette er en toString() funksjon slik som vi er kjent med ifra Java
    # Om dere prøver å kommentere den ut vil dere kunne observere i /admin
    # at objektene, i dette tilfellet manufacturer kun vises som generiske objekter,
    # i stedet for ved navn
    def __str__(self):
        return self.name





class Engine(models.Model):
    name = models.CharField(max_length=120)
    propellant = models.CharField(max_length=120)
    # IntegerField er standard felt for heltall
    isp_sl = models.IntegerField(null=True, blank=True)
    isp_vacuum = models.IntegerField(null=True, blank=True)
    thrust_sl = models.IntegerField(null=True, blank=True)
    thrust_vacuum = models.IntegerField(null=True, blank=True)
    # FloatField er standard felt for flyttall
    chamber_pressure = models.FloatField(null=True, blank=True)
    # ForeignKey er en måte å opprette relasjon på. Her vil en manufacturer ha mange engines
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)

    def __str__(self):
        return self.name


class LaunchPlatform(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    engine = models.ForeignKey(Engine, null=True, blank=True)

    def __str__(self):
        return self.name