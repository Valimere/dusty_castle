from django import forms
from django.utils import timezone
from .models import Player, Tournament


class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['email', 'first_name', 'last_name']


class PlayerSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class TournamentRegistrationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date()
    )
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'status']


class TournamentSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
