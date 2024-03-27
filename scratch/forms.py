from django import forms
from .models import Player, TournamentRegistration


class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['email', 'first_name', 'last_name']


class PlayerSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class TournamentRegistrationForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.none())  # Empty queryset initially

    def __init__(self, *args, **kwargs):
        tournament_id = kwargs.pop('tournament_id', None)
        super(TournamentRegistrationForm, self).__init__(*args, **kwargs)
        if tournament_id:
            # Fetching IDs of players already registered in this tournament
            registered_players = TournamentRegistration.objects.filter(
                tournament_id=tournament_id).values_list('player', flat=True)

            # Excluding these players from the dropdown
            self.fields['player'].queryset = Player.objects.exclude(id__in=registered_players)


class TournamentSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
