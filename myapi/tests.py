import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from catalog.models import BoardGames, Category

pytestmark = pytest.mark.django_db


class TestBoardGamesAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_game_API(self):
        BoardGames.objects.create(name='test_game')
        test_game = BoardGames.objects.get(name='test_game')
        response = self.client.get('/all_games/')
        assert response.json != None
        assert response.status_code == 200

    def test_category_API(self):
        Category.objects.create(name='test_category')
        category = Category.objects.get(name='test_category')
        response = self.client.get('/all_category/')
        print(response)
        assert response.json != None
        assert response.status_code == 200
