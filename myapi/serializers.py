from catalog.models import BoardGames, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class BoardGamesSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_likes = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = BoardGames
        fields = "__all__"


class CategoryGamesSerializer(serializers.HyperlinkedModelSerializer):
    boardgames_set = BoardGamesSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    game_likes = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ["username", "id", "first_name", "last_name", "email", "game_likes"]
