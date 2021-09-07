from django.contrib import admin

from catalog.models import BoardGames, Category, Comment

admin.site.register(BoardGames)
admin.site.register(Category)
admin.site.register(Comment)
