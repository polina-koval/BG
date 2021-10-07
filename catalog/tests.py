import datetime

import pytest
from django.test import TestCase

from catalog.models import Category, BoardGames, Comment


class CategoryTestCase(TestCase):
    def test_category(self):
        Category.objects.create(name="test_category")
        test = Category.objects.get(name="test_category")
        assert test.name == 'test_category'


class BoardGamesTestCase(TestCase):
    def test_game(self):
        BoardGames.objects.create(name='test_game')
        test_game = BoardGames.objects.get(name='test_game')
        assert test_game.name == 'test_game'
        assert test_game.start_player_age == 0
        assert test_game.category.all().count() == 0


class TestModels(TestCase):
    def test_game_has_an_category(self):
        game = BoardGames.objects.create(name='Catan')
        strategy = Category.objects.create(name='strategy')
        game.category.add(strategy)
        assert game.category.count() == 1
        assert game.category.all()[0].name == 'strategy'
        assert game.name == 'Catan'


class TestStr(TestCase):
    def test_str_is_equal_to_category_name(self):
        Category.objects.create(name='strategy')
        category = Category.objects.get(name='strategy')
        assert str(category) == category.name

    def test_str_is_equal_to_board_games_name(self):
        BoardGames.objects.create(name='test game')
        game = BoardGames.objects.get(name='test game')
        assert str(game) == game.name

    def test_str_comment(self):
        game = BoardGames.objects.create(name='Test Game')
        comment = Comment.objects.create(name='Test Name', body='Test comment', date_added=datetime.datetime.now(),
                                         game_id=1)
        game.comments.add(comment)
        assert str(comment) == f"{comment.game.name} - {comment.name}"


class TestMethodBoardGames(TestCase):
    def test_value_error(self):
        with pytest.raises(ValueError) as excinfo:
            game1 = BoardGames.objects.create(name='Catan')
            game2 = BoardGames.objects.create(name='Catan')
        assert 'This game already exists' in str(excinfo.value)

    def test_game_is_recommend(self):
        game1 = BoardGames.objects.create(name='Test Game1', rating_from_the_store=10)
        game2 = BoardGames.objects.create(name='Test Game2', rating_from_the_store=2)
        assert game1.recommendation() == '(Recommend)'
        assert game2.recommendation() == ''

    def test_age_check(self):
        game_1 = BoardGames.objects.create(name='Test Game1', start_player_age=18)
        game_2 = BoardGames.objects.create(name='Test Game2', start_player_age=10)
        assert game_1.age_check() == 'Caution, for adults only!'
        assert game_2.age_check() == ''

    def test_total_likes(self):
        game1 = BoardGames.objects.create(name='Test Game1')
        assert game1.total_likes() == 0


class TestURL(TestCase):
    def test_view_category_list(self):
        response = self.client.get('/catalog/')
        assert response.status_code == 200

    def test_view_game_list_in_category(self):
        game = BoardGames.objects.create(name='Test Game')
        duel = Category.objects.create(name='Test Category')
        game.category.add(duel)
        response1 = self.client.get('/catalog/category/1/')
        response2 = self.client.get('/catalog/description/1/')
        assert response1.status_code == 200
        assert response2.status_code == 200

    def test_view_search_result(self):
        test_game1 = BoardGames.objects.create(name='TestGame1')
        test_game2 = BoardGames.objects.create(name='TestGame2', description="TestDescriptionForGame")
        response1 = self.client.get('/catalog/search/?q=TestGame1/')
        response2 = self.client.get('/catalog/search/?q=TestDescriptionForGame/')
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert test_game1.name in str(response1.request)
        assert test_game2.description in str(response2.request)

