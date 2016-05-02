from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

GAME_STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First player wins'),
    ('S', 'Second player wins'),
    ('D', 'Draw')
)

# Create your models here.
class GamesManager(models.Manager):
    def games_for_user(self, user):
        """Return a queryset of games that this user participates in"""
        return super(GamesManager, self).get_queryset().filter(
            Q(first_player_id=user.id) | Q(second_player_id=user.id))

class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player")
    second_player = models.ForeignKey(User, related_name="games_second_player")
    next_to_move = models.ForeignKey(User, related_name="games_to_move")
    start_time = models.DateTimeField(auto_now=True)
    last_active = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=1, default='A', choices=GAME_STATUS_CHOICES)

    objects = GamesManager()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)

