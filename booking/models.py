from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=256, null=True, blank=True)
    genre = models.CharField(max_length=120)
    tech_needs = models.TextField(max_length=256, null=True, blank=True)
    concert_id = models.ForeignKey('Concert', null=True, blank=True)
    festival_id = models.ForeignKey('Festival', null=True, blank=True)


class Concert(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=120, null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    stage_id = models.ForeignKey('Stage', null=True, blank=True)
    sold_tickets = models.IntegerField(null=True, blank=True)
    audience_showed_up = models.IntegerField(null=True, blank=True)
    concert_start_time = models.DateTimeField(null=True, blank=True)
    concert_end_time = models.DateTimeField(null=True, blank=True)
    tech_meetup_time = models.DateTimeField(null=True, blank=True)
    tech_done_time = models.DateTimeField(null=True, blank=True)
    festival_id = models.ForeignKey('Festival', null=True, blank=True)
    technicians = models.ManyToManyField(User, blank=True)

    # number_of_tech = models.IntegerField(null=True, blank=True)

    # Not the best solution, should implement validation with clear.All() Method
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stage_id.audience_cap < self.sold_tickets:
            raise Exception("Cant add more tickets than stage capacity")
        else:
            super(Concert, self).save()

    def __str__(self):
        return self.name


class Festival(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    tickets = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=120, null=True, blank=True)
    audience_cap = models.IntegerField(null=True, blank=True)
    festival_id = models.ForeignKey(Festival, null=True, blank=True)
    # Do we need schedule here?

    def __str__(self):
        return self.name
