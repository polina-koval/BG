from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, default="Without category")
    picture = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        verbose_name = "Category name"
        verbose_name_plural = "Category names"

    def __str__(self):
        return self.name


class BoardGames(models.Model):
    name_of_game = models.CharField(max_length=200)
    start_player_age = models.IntegerField(default=0)
    rating_from_the_store = models.IntegerField(default=0)
    game_description = models.TextField(default="Let's add later")
    category = models.ManyToManyField(Category)
    picture = models.ImageField(upload_to="images/", blank=True)
    playing_time = models.IntegerField(default=0)
    min_players_number = models.IntegerField(default=1)
    max_players_number = models.IntegerField(default=100)
    likes = models.ManyToManyField(User, related_name="game_likes")

    class Meta:
        verbose_name = "Board Game"
        verbose_name_plural = "Board Games"

    def __str__(self):
        return self.name_of_game

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    game = models.ForeignKey(
        BoardGames, related_name="comments", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name_of_game} - {self.name}"
