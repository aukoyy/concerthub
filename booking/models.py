from django.db import models
from django.contrib.auth.models import User
from datetime import date
from .validators import validate_future


class Artist(models.Model):
    name = models.CharField(max_length=120, blank=False)
    genre = models.ForeignKey('Genre', null=True, blank=True)
    artist_manager = models.ForeignKey(User, null=True, related_name='artist_manager',
                                       limit_choices_to={'groups__name': 'artist_manager'})
    artist_rev = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BookingOffer(models.Model):
    artist = models.ForeignKey(Artist, null=True, related_name='artist')
    artist_manager = models.ForeignKey(User, default=1, limit_choices_to={'groups__name': 'artist_manager'})
    comment = models.TextField(max_length=120, blank=True)
    time_slot = models.ForeignKey('TimeSlot', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    tech_needs = models.TextField(blank=True)
    approved_by_bm = models.BooleanField(default=False)
    accepted_by_am = models.BooleanField(default=False)
    booker = models.ForeignKey(User, related_name='booker', limit_choices_to={'groups__name': 'booker'})
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        return "booking/booking"

    def __str__(self):
        return "%s offer at %s" % (self.artist, self.time_slot)

    class Meta:
        ordering = ('time_slot', 'time_slot__stage')


class Concert(models.Model):
    artist = models.ForeignKey(Artist)
    time_slot = models.OneToOneField('TimeSlot', null=True, blank=True,)
    description = models.TextField(max_length=120, null=False, blank=True)
    technicians = models.ManyToManyField(User, blank=True, limit_choices_to={'groups__name': 'technician'})
    techs_met = models.ManyToManyField(User, blank=True, related_name='techs_met',
                                       limit_choices_to={'groups__name': 'technician'})
    tech_meetup_time = models.DateTimeField(null=True, blank=True)
    tech_done_time = models.DateTimeField(null=True, blank=True)
    sold_tickets = models.IntegerField(null=True, blank=True)
    audience_showed_up = models.IntegerField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    costs = models.FloatField(null=True, blank=True)
    festival = models.ForeignKey('Festival', default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('time_slot__start_date', 'time_slot__stage', 'artist',)

    def __str__(self):
        return '%s playing at %s on %s' % (self.artist, self.time_slot.stage, self.time_slot.start_date)

    @property
    def is_in_future(self):
        if self.time_slot.start_date >= date.today():
            return True
        else:
            return False


class Festival(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True, validators=[validate_future])
    end_date = models.DateField(null=True, blank=True)
    num_of_concerts = models.IntegerField(null=True, blank=True)
    total_revenue = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=120, null=False, blank=True)
    audience_cap = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    # Time Slots will be individual to each concert, so stage A will have slots A1, A2, A3...
    # A1 can not be used on stage B.
    start_date = models.DateField(null=True, blank=False, validators=[validate_future])
    end_date = models.DateField(null=True, blank=False)
    start_time = models.TimeField(null=True, blank=False)
    end_time = models.TimeField(null=True, blank=False)
    stage = models.ForeignKey(Stage, null=True, blank=False)

    def get_absolute_url(self):
        return("booking/booking_overview")

    def __str__(self):
        day = self.start_date.day
        month = self.start_date.month
        start = '%02d:%02d' % (self.start_time.hour, self.start_time.minute)
        end = '%02d:%02d' % (self.end_time.hour, self.end_time.minute)
        return '%s:  %s/%s %s-%s' % (self.stage, day, month, start, end)

    class Meta:
        ordering = ('start_date', 'start_time', 'stage',)

