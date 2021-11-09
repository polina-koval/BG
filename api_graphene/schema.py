import graphene
from graphene_django import DjangoListField, DjangoObjectType

from accounts.models import UserProfile
from catalog.models import BoardGames, Category, Comment


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class GamesType(DjangoObjectType):
    class Meta:
        model = BoardGames
        fields = "__all__"


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = "__all__"


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_board_games = graphene.List(GamesType)
    all_comments = graphene.List(CommentType)
    all_users = graphene.List(UserType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_board_games(self, info, **kwargs):
        return BoardGames.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return UserProfile.objects.all()


schema = graphene.Schema(query=Query)
