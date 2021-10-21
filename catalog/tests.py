import datetime
from unittest.mock import patch

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from catalog.factories import BoardGamesFactory, CategoryFactory
from catalog.models import Comment, UserProfile


class CategoryTestCase(TestCase):

    def test_category(self):
        category = CategoryFactory(name='test_category')
        assert category.name == 'test_category'


class BoardGamesTestCase(TestCase):

    def test_game(self):
        game = BoardGamesFactory(name="test_game")
        assert game.name == "test_game"
        assert game.start_player_age == 0
        assert game.category.all().count() == 0


class TestModelsBoardGamesCategoryTogether(TestCase):
    def test_game_has_an_category(self):
        game = BoardGamesFactory(name='Catan')
        strategy = CategoryFactory(name='strategy')
        game.category.add(strategy)
        assert game.category.count() == 1
        assert game.category.all()[0].name == 'strategy'
        assert game.name == 'Catan'


class TestStr(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user",
                                             email="user1@test.com")
        self.user.set_password("password1")
        self.user.save()
        self.client.login(username="test_user", password="password1")

    def test_str_is_equal_to_category_name(self):
        category = CategoryFactory(name='strategy')
        assert str(category) == category.name

    def test_str_is_equal_to_board_games_name(self):
        game = BoardGamesFactory(name='test game')
        assert str(game) == game.name

    def test_str_comment(self):
        game = BoardGamesFactory(name='Test Game')
        test_user = UserProfile.objects.get(username='test_user')
        comment = Comment.objects.create(body='Test comment',
                                         date_added=datetime.datetime.now(),
                                         game_id=1)
        game.comments.add(comment)
        test_user.comment_set.add(comment)
        assert str(comment) == f"{comment.game.name} - {comment.owner}"


class TestMethodBoardGames(TestCase):

    def test_value_error(self):
        with pytest.raises(ValueError) as excinfo:
            category = CategoryFactory()
            BoardGamesFactory(name="CATAN", category=(category,))
            BoardGamesFactory(name="Catan", category=(category,))
            assert "This game already exists" in str(excinfo.value)

    def test_game_is_recommend(self):
        game1 = BoardGamesFactory(rating_from_the_store=10)
        game2 = BoardGamesFactory(rating_from_the_store=2)
        assert game1.recommendation() == '(Recommend)'
        assert game2.recommendation() == ''

    def test_age_check(self):
        game_1 = BoardGamesFactory(start_player_age=18)
        game_2 = BoardGamesFactory(start_player_age=10)
        assert game_1.age_check() == 'Caution, for adults only!'
        assert game_2.age_check() == ''

    def test_total_likes(self):
        game1 = BoardGamesFactory(name='Test Game1')
        assert game1.total_likes() == 0

    @patch('catalog.models.datetime.date')
    def test_is_sale(self, mock_date):
        mock_date.today.return_value = \
            datetime.datetime(year=2021, month=10, day=15)  # Friday
        game = BoardGamesFactory(price=100, rating_from_the_store=5)
        assert game.is_sale == ''
        assert game.price == 100
        game.rating_from_the_store = 2
        assert game.is_sale == 'Sale'
        assert game.price == 80


class TestURL(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user",
                                             email="user1@test.com")
        self.user.set_password("password1")
        self.user.save()
        self.client.login(username="test_user", password="password1")

    def test_view_category_list(self):
        response = self.client.get('/catalog/')
        assert response.status_code == 200

    def test_view_game_list_in_category(self):
        game = BoardGamesFactory(name='Test Game')
        duel = CategoryFactory(name='Test Category')
        game.category.add(duel)
        response1 = self.client.get('/catalog/category/1/')
        response2 = self.client.get('/catalog/description/1/')
        assert response1.status_code == 200
        assert response2.status_code == 200

    def test_view_search_result(self):
        test_game1 = BoardGamesFactory(name='TestGame1')
        test_game2 = BoardGamesFactory(name='TestGame2',
                                       description="TestDescriptionForGame")
        response1 = self.client.get('/catalog/search/?q=TestGame1/')
        response2 = self.client.get(
            '/catalog/search/?q=TestDescriptionForGame/')
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert test_game1.name in str(response1.request)
        assert test_game2.description in str(response2.request)

    def test_view_like_games(self):
        test_user = User.objects.get(username='test_user')
        game = BoardGamesFactory(name='Catan')
        game.likes.add(test_user.id)
        response_1 = self.client.get("/accounts/dashboard/1/likes_games")
        assert game.likes.count() == 1
        assert game.likes.get(id=test_user.id) == test_user
        assert response_1.status_code == 200
        response_2 = self.client.get(reverse('catalog:like_game',
                                             args=[str(game.pk)]))
        assert response_2.status_code == 302
        assert game.likes.count() == 0
        self.client.get(reverse('catalog:like_game', args=[str(game.pk)]))
        assert game.likes.count() == 1
