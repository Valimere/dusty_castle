from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("register/", views.register_player_view, name="register"),
    path("registered_players/", views.registered_players, name="registered_players")
]