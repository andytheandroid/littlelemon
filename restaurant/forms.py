from django import forms


class BookingForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    numberofguests = forms.IntegerField(label="Number of guests")
    date = forms.DateField(label="Reservation date")
