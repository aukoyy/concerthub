from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name





class Engine(models.Model):
    name = models.CharField(max_length=120)
    propellant = models.CharField(max_length=120)
    isp = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)

    def __str__(self):
        return self.name


class LaunchPlatform(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    engine = models.ForeignKey(Engine, null=True, blank=True)

    def __str__(self):
        return self.name