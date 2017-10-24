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


    def clean(self):
        cleaned_data = super(TimeSlotForm, self).clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        stage = cleaned_data.get('stage')
        conflicts = TimeSlot.objects.filter(
            start_time__lte=end_time,
            end_time__gte=start_time,
            start_date__lte=start_date,
            end_date__gte=end_date,
            stage=stage,
        )
        if any(conflicts):
            raise forms.ValidationError("%i conflicts found" % conflicts.count())
        return cleaned_data
