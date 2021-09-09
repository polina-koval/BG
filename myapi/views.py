from catalog.models import BoardGames, Category
from rest_framework import viewsets

from myapi.serializers import BoardGamesSerializer, CategoryGamesSerializer


class CategoryGamesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategoryGamesSerializer


class BoardGamesViewSet(viewsets.ModelViewSet):
    queryset = BoardGames.objects.all().order_by("name_of_game")
    serializer_class = BoardGamesSerializer
