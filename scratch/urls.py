from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("registered_players/", views.registered_players_view, name="registered_players"),
    path("registered_tournaments/", views.registered_tournaments_view, name="registered_tournaments"),
    path("tournament_registration/", views.register_tournament_view, name="tournament_registration"),
    path("player_registration/", views.register_player_view, name="player_registration"),

]