from django.contrib import admin

from catalog.models import BoardGames, Category, Comment


@admin.register(BoardGames)
class BoardGamesAdmin(admin.ModelAdmin):
    actions = ['make_published', 'make_draft']

    @admin.action(description='Mark selected games as published')
    def make_published(self, request, queryset):
        queryset.update(status='Published')

    @admin.action(description='Mark selected games as draft')
    def make_draft(self, request, queryset):
        queryset.update(status='Draft')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
