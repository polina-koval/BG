import factory
from catalog.models import Category, BoardGames


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category #%s" % n)


class BoardGamesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardGames

    name = factory.Sequence(lambda n: "Game #%s" % n)
    description = factory.Sequence(lambda n: "Description #%s" % n)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.category.add(*extracted)