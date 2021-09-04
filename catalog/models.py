from django.db import models
from accounts.models import UserProfile
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, default='Without category')
    picture = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Category name'
        verbose_name_plural = 'Category names'

    def __str__(self):
        return self.name


class BoardGames(models.Model):
    name_of_game = models.CharField(max_length=200)
    start_player_age = models.IntegerField(default=0)
    rating_from_the_store = models.IntegerField(default=0)
    game_description = models.TextField(default="Let's add later")
    category = models.ManyToManyField(Category)
    picture = models.ImageField(upload_to='images/', blank=True)
    playing_time = models.IntegerField(default=0)
    min_players_number = models.IntegerField(default=1)
    max_players_number = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'Board Game'
        verbose_name_plural = 'Board Games'

    def __str__(self):
        return self.name_of_game


class Comment(models.Model):
    game = models.ForeignKey(
        BoardGames, on_delete=models.PROTECT, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    content = models.TextField(max_length=240)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
