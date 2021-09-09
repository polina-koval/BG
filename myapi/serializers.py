from catalog.models import BoardGames, Category
from rest_framework import serializers


class CategoryGamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class BoardGamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardGames
        fields = ("name_of_game", "category", "playing_time", "rating_from_the_store")
