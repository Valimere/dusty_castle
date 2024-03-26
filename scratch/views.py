from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import PlayerRegistrationForm, PlayerSearchForm, TournamentRegistrationForm, TournamentSearchForm
from .models import Player, Tournament


def register_player_view(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registered_players')
        else:
            # If the form is not valid, form.errors will contain all error messages
            return render(request, 'scratch/player_registration.html', {'form': form})
    else:
        form = PlayerRegistrationForm()
        return render(request, 'scratch/player_registration.html', {'form': form})


def registered_players_view(request):
    search_form = PlayerSearchForm(request.GET)
    players = Player.objects.all()
    if search_form.is_valid():
        search = search_form.cleaned_data.get('search')
        if search:
            players = players.filter(
                Q(email__icontains=search) |
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search)
            )
    return render(request,
                  template_name='scratch/registered_players.html',
                  context={'players': players, 'form': search_form})


def register_tournament_view(request):
    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registered_tournaments')
        else:
            return render(request, 'scratch/tournament_registration.html', {'form': form})
    else:
        form = TournamentRegistrationForm()
        return render(request, 'scratch/tournament_registration.html', {'form': form})


def registered_tournaments_view(request):
    search_form = TournamentSearchForm(request.GET)
    tournaments = Tournament.objects.all()
    if search_form.is_valid():
        name_search = search_form.cleaned_data.get('search')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if name_search:
            tournaments = tournaments.filter(name__icontains=name_search)
        if start_date and end_date:
            tournaments = tournaments.filter(date__range=(start_date, end_date))

    return render(request,
                  template_name='scratch/registered_tournaments.html',
                  context={'tournaments': tournaments, 'search_form': search_form})


def IndexView(request):
    return render(request, 'scratch/base.html')

