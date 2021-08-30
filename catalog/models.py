from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200, default='Without category')

    class Meta:
        verbose_name = 'Category name'
        verbose_name_plural = 'Category names'

    def __str__(self):
        return self.category_name


class BoardGames(models.Model):
    name_of_game = models.CharField(max_length=200)
    start_player_age = models.IntegerField(default=0)
    rating_from_the_store = models.IntegerField(default=0)
    game_description = models.TextField(default="Let's add later")
    category = models.ManyToManyField(Category)
    picture = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Board Game'
        verbose_name_plural = 'Board Games'

    def __str__(self):
        return self.name_of_game
