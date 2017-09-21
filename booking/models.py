from django.db import models
from django.core.exceptions import ValidationError

class Stage(models.Model):
    name = models.CharField(max_length=120)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name

class Concert(models.Model):
    artist = models.CharField(max_length=120)
    stage = models.ForeignKey(Stage)
    date = models.DateField(null=True, blank=True)
    concert_start_time = models.TimeField(null=True, blank=True)
    concert_end_time = models.TimeField(null=True, blank=True)
    tickets = models.IntegerField(null=True, blank=True)
    number_of_tech = models.IntegerField(null=True, blank=True)

    #Cheeky solution, switch to .clean() when enough knowledge.
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stage.capacity < self.tickets:
            raise Exception("Cant add more tickets than stage capacity")
        else:
            super(Concert, self).save()

    def __str__(self):
        return self.artist