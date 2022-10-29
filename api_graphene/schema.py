import graphene
from graphene_django import DjangoListField, DjangoObjectType

from accounts.models import UserProfile
from catalog.models import BoardGames, Category, Comment


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class BoardGamesType(DjangoObjectType):
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
    game_by_name = DjangoListField(
        BoardGamesType, name=graphene.String(required=True)
    )
    games_in_category = DjangoListField(
        BoardGamesType, category=graphene.String(required=True)
    )
    all_categories = graphene.List(CategoryType)
    all_board_games = graphene.List(BoardGamesType)
    all_comments = graphene.List(CommentType)
    all_users = graphene.List(UserType)

    def resolve_games_in_category(self, info, category):
        return BoardGames.objects.filter(category__name__icontains=category)

    def resolve_game_by_name(self, info, name):
        return BoardGames.objects.filter(name=name)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_board_games(self, info, **kwargs):
        return BoardGames.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return UserProfile.objects.all()


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class BoardGamesInput(graphene.InputObjectType):
    name = graphene.String()
    category = graphene.String()


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_data=None):
        category = Category.objects.create(
            name=category_data.name,
        )
        return CreateCategory(category=category)


class CreateBoardGames(graphene.Mutation):
    boardgames = graphene.Field(BoardGamesType)

    class Arguments:
        board_games_data = BoardGamesInput(required=True)

    @staticmethod
    def mutate(root, info, board_games_data=None):
        category, _ = Category.objects.get_or_create(
            name=board_games_data.category
        )
        boardgames = BoardGames.objects.create(
            name=board_games_data.name,
        )
        boardgames.category.add(category)
        return CreateBoardGames(boardgames=boardgames)


class Mutations(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_boardgames = CreateBoardGames.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
