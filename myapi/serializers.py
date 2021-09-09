from catalog.models import BoardGames, Category
from rest_framework import serializers


class CategoryGamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BoardGamesSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_likes = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = BoardGames
        fields = "__all__"
