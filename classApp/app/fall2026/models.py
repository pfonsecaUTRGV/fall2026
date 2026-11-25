from django.db import models
from django.conf import settings


class Task(models.Model):
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=8)

	def __str__(self):
		return self.title

class PokemonTeam(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pokemon_teams"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TeamPokemon(models.Model):
    team = models.ForeignKey(
        PokemonTeam,
        on_delete=models.CASCADE,
        related_name="members"
    )
    pokemon_id = models.PositiveIntegerField()
    pokemon_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pokemon_name
