

from django import forms


class InventoryLoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)