from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PlayerRegistrationForm, PlayerSearchForm
from .models import Player


def register_player_view(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registered_players')
        else:
            # If the form is not valid, form.errors will contain all error messages
            return render(request, 'scratch/register.html', {'form': form})
    else:
        form = PlayerRegistrationForm()
        return render(request, 'scratch/register.html', {'form': form})


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

def IndexView(request):
    return HttpResponse("scratch index")
