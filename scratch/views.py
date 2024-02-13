from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PlayerRegistrationForm
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


def registered_players(request):
    players = Player.objects.all()
    return render(request,
                  template_name='scratch/registered_players.html',
                  context={'players': players})


def IndexView(request):
    return HttpResponse("scratch index")
