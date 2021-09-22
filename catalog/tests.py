from django.test import TestCase
from catalog.models import Category, BoardGames


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="test_category")

    def test_category(self):
        test = Category.objects.get(name="test_category")
        self.assertEqual(test.name, 'test_category')


class BoardGamesTestCase(TestCase):
    def setUp(self):
        BoardGames.objects.create(name='test_game')

    def test_game(self):
        test_game = BoardGames.objects.get(name='test_game')
        self.assertEqual(test_game.name, 'test_game')
        self.assertEqual(test_game.start_player_age, 0)
        self.assertEqual(test_game.category.all().count(), 0)


class TestModels(TestCase):
    def test_game_has_an_category(self):
        game = BoardGames.objects.create(name='Catan')
        strategy = Category.objects.create(name='strategy')
        game.category.add(strategy)
        self.assertEqual(game.category.count(), 1)
        self.assertEqual(game.category.all()[0].name, 'strategy')
        self.assertEqual(game.name, 'Catan')
