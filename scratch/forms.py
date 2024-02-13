from django import forms
from .models import Player


class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['email', 'first_name', 'last_name']