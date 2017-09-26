from django.db import models


class Stage(models.Model):
    name = models.CharField(max_length=120)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Festival(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    tickets = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.name


class Concert(models.Model):
    artist = models.CharField(max_length=120)
    stage = models.ForeignKey(Stage)
    date = models.DateField(null=True, blank=True)
    concert_start_time = models.TimeField(null=True, blank=True)
    concert_end_time = models.TimeField(null=True, blank=True)
    tickets = models.IntegerField(null=True, blank=True)
    number_of_tech = models.IntegerField(null=True, blank=True)
    festival = models.ForeignKey(Festival, null=True, blank=True)

    # Not the best solution, should implement validation with clear.All() Method
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stage.capacity < self.tickets:
            raise Exception("Cant add more tickets than stage capacity")
        else:
            super(Concert, self).save()

    def __str__(self):
        return self.artist
