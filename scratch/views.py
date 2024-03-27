from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerRegistrationForm, PlayerSearchForm, TournamentRegistrationForm, TournamentSearchForm, TournamentRegistration
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


def tournament_view(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    player_registration_form = TournamentRegistrationForm(
        request.POST or None,
        tournament_id=tournament_id  # Passing tournament_id to the form
    )
    if request.method == 'POST' and player_registration_form.is_valid():
        player = player_registration_form.cleaned_data['player']

        # Create a TournamentRegistration instance instead of using .add()
        TournamentRegistration.objects.create(
            player=player,
            tournament=tournament,
            registration_date=timezone.now().date()  # Set the registration date
        )
        return redirect('tournament_detail', tournament_id=tournament.id)

    context = {
        'tournament': tournament,
        'player_registration_form': player_registration_form,
        'registered_players': tournament.registered_players.all(),
    }
    return render(request, 'scratch/tournament_detail.html', context)


def tournament_delete_view(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        tournament.delete()
        return redirect('registered_tournaments')

    return redirect('tournament_detail', tournament_id=tournament.id)


def delete_player_from_tournament(request, tournament_id, player_id):
    if request.method == 'POST':
        tournament = get_object_or_404(Tournament, id=tournament_id)
        player = get_object_or_404(Player, id=player_id)
        tournament.registered_players.remove(player)
        return redirect('tournament_detail', tournament_id=tournament.id)
    # Redirect or show an error if not POST request


def IndexView(request):
    return render(request, 'scratch/base.html')

