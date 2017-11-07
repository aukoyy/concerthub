from django import forms

from .models import TimeSlot


class TimeSlotForm(forms.ModelForm):
    start_date = forms.DateField(required=True, label="Start Date", widget=forms.SelectDateWidget)
    end_date = forms.DateField(required=True, label="End Date", widget=forms.SelectDateWidget)
    start_time = forms.TimeField(required=True, label="Start Time", widget=forms.TextInput({"placeholder": " H : M "}))
    end_time = forms.TimeField(required=True, label="End_Time", widget=forms.TextInput({"placeholder": " H : M "}))

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
        if self.instance.pk is not None:
            conflicts = conflicts.exclude(pk=self.instance.pk)
        if any(conflicts):
            raise forms.ValidationError("You are trying to add a timeslot to a time and on a stage that is already "
                                        "taken by %i other time slots. Please choose another time and/or stage"
                                        % conflicts.count())
        return cleaned_data

