from django.db import models


class Player(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.email


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    p1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams_p1')
    p2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams_p2')


class Tournament(models.Model):
    NOT_STARTED = 'Not started'
    STARTED = 'Started'
    COMPLETED = 'Completed'

    TOURNAMENT_STATUS_CHOICES = [
        (NOT_STARTED, 'Not started'),
        (STARTED, 'Started'),
        (COMPLETED, 'Completed')
    ]

    name = models.CharField(unique=True, max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=12, choices=TOURNAMENT_STATUS_CHOICES, default=NOT_STARTED)
    registered_players = models.ManyToManyField(
        Player,
        through='TournamentRegistration',
        related_name='tournaments'
    )


class TournamentRegistration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registration_date = models.DateField()

