from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class BookingForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    number_of_guests = forms.IntegerField(label="Number of guests")
    reservation_date = forms.DateField(label="Reservation date")


class LoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
