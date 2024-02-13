from django.db import models


class Player(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    p1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams_p1')
    p2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams_p2')


class Tournament(models.Model):
    name = models.CharField(unique=True, max_length=200)
    date = models.DateField()
