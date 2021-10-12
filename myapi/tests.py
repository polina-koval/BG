from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from catalog.models import BoardGames, Category


class TestBoardGamesAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", email="user1@test.com", is_staff=True)
        self.user.set_password("password1")
        self.user.save()

    def test_game_API(self):
        self.client.force_authenticate(self.user)
        BoardGames.objects.create(name='test_game777')
        response = self.client.get('/all_games/')
        assert response.json() is not None
        assert response.status_code == 200

    def test_category_API(self):
        self.client.force_authenticate(self.user)
        Category.objects.create(name='test_category')
        response = self.client.get('/all_category/')
        assert response.json() is not None
        assert response.status_code == 200

    fixtures = ["fixtures.json"]

    def test_load_data(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/all_games/")
        test_game = BoardGames.objects.get(name="Party")
        assert "Party", "Duel" in response.json()
        assert test_game.name == "Party", test_game.model == "catalog.boardgames"
        assert response.status_code == 200
