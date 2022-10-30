from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from accounts.models import Cart, Receipt
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

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    readonly_fields = ['unique_number']
