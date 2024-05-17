from django import forms


class BookingForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    number_of_guests = forms.IntegerField(label="Number of guests")
    reservation_date = forms.DateField(label="Reservation date")


class LoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)