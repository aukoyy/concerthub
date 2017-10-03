from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Artist(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    description = models.TextField(max_length=256, null=False, blank=True)
    genre = models.CharField(max_length=120, null=False, blank=True)
    concert = models.ForeignKey('Concert', null=True, blank=True)
    festival = models.ForeignKey('Festival', null=True, blank=True)
    artist_manager = models.ForeignKey(User, null=True, blank=True)
    time_slot = models.OneToOneField('TimeSlot', null=True, blank=True)

    def __str__(self):
        return self.name


class BookingOffer(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    artist = models.OneToOneField(Artist, null=True, blank=True)
    comment = models.TextField(max_length=120, null=False, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    offering_time = models.ForeignKey('TimeSlot', null=True, blank=True)
    offering_price = models.IntegerField(null=True, blank=True)
    tech_needs = models.TextField(null=False, blank=True)
    approved_by_bm = models.BooleanField(blank=False, default=False)
    accepted_by_am = models.BooleanField(blank=False, default=False)
    artist_manager = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.name


class Concert(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=120, null=False, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    stage = models.ForeignKey('Stage', null=True, blank=True)
    sold_tickets = models.IntegerField(null=True, blank=False)
    audience_showed_up = models.IntegerField(null=True, blank=True)
    tech_meetup_time = models.DateTimeField(null=True, blank=True)
    tech_done_time = models.DateTimeField(null=True, blank=True)
    festival = models.ForeignKey('Festival', null=True, blank=True)
    technicians = models.ManyToManyField(User, blank=True)
    time_slot = models.OneToOneField('TimeSlot', null=True, blank=True)

    # number_of_tech = models.IntegerField(null=True, blank=True)

    # Not the best solution, should implement validation with clear.All() Method
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stage.audience_cap < self.sold_tickets:
            raise Exception("Cant add more tickets than stage capacity")
        else:
            super(Concert, self).save()

    def __str__(self):
        return self.name

    @property
    def is_in_future(self):
        # Using the starting time of Concert object
        if self.concert_start_time.date() >= date.today():
            # print('It is in the future')
            return True
        else:
            # print('It is in the past')
            return False

    class Meta:
        ordering = ('concert_start_time', 'name',)


class Festival(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    tickets = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=120, null=False, blank=True)
    audience_cap = models.IntegerField(null=True, blank=False)
    festival = models.ForeignKey(Festival, null=True, blank=True)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    # Time Slots will be individual to each concert, so stage A will have slots A1, A2, A3...
    # A1 can not be used on stage B.
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    start_time = models.TimeField(null=True, blank=False)
    end_time = models.TimeField(null=True, blank=False)
    stage = models.ForeignKey(Stage, null=True, blank=False)

    def __str__(self):
        return "%s - %s" % (self.start_time, self.end_time)
