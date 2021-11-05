from django.contrib import admin

from catalog.models import BoardGames, Category, Comment


@admin.register(BoardGames)
class BoardGamesAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
