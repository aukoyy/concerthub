from django import forms

from .models import TimeSlot


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = [
            'start_date',
            'end_date',
            'start_time',
            'end_time',
            'stage',
        ]
