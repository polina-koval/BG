import datetime
from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile

ADULTHOOD = 18
SALE_DAY = 'Friday'
RATING_FOR_RECOMMENDATION = 8
RATING_FOR_DISCOUNT = 2


class Category(models.Model):
    name = models.CharField(max_length=200, default="Without category")
    picture = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        verbose_name = "Category name"
        verbose_name_plural = "Category names"

    def __str__(self):
        return self.name


class LowCostGamesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__lt=5)


class BoardGames(models.Model):
    name = models.CharField(max_length=200)
    start_player_age = models.IntegerField(default=0)
    description = models.TextField(default="Let's add later")
    category = models.ManyToManyField(Category)
    picture = models.ImageField(upload_to="images/", blank=True)
    playing_time = models.IntegerField(default=0)
    min_players_number = models.IntegerField(default=1)
    max_players_number = models.IntegerField(default=100)
    likes = models.ManyToManyField(User, related_name="game_likes", blank=True)
    price = models.IntegerField(default=0)

    class StoreRating(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
        Six = 6
        Seven = 7
        Eight = 8
        Nine = 9
        Ten = 10

    class StatusChoices(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISHED = 'Published'

    rating_from_the_store = models.IntegerField(choices=StoreRating.choices,
                                                default=1)
    status = models.CharField(max_length=10, choices=StatusChoices.choices,
                              default='Draft')
    objects = models.Manager()
    cheap_games = LowCostGamesManager()
    data = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = "Board Game"
        verbose_name_plural = "Board Games"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if (
            BoardGames.objects.filter(name__icontains=self.name).exists()
            and self.id is None
        ):
            raise ValueError("This game already exists")
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def recommendation(self):
        return '(Recommend)' if self.rating_from_the_store >= \
                                RATING_FOR_RECOMMENDATION else ''

    @property
    def is_sale(self):
        today = datetime.date.today().strftime('%A')
        if today == SALE_DAY and self.rating_from_the_store < 4:
            self.price = 0.8 * self.price  # 20% discount
            return 'Sale'
        return ''

    def age_check(self):
        return 'Caution, for adults only!' if self.start_player_age >=\
                                               ADULTHOOD else ''


class Comment(models.Model):
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    game = models.ForeignKey(
        BoardGames, related_name="comments", on_delete=models.CASCADE
    )
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name} - {self.owner}"
