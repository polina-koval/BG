from django.template import loader
from django.shortcuts import render
from django.db.models import Count

from .models import BoardGames, Category


def game_list(request, category_id):
    games = BoardGames.objects.filter(category=category_id)
    context = {
        'games': games,
    }
    return render(request, 'catalog/game_list.html', context)


def category_list(request):
    latest_category_list = Category.objects.all()
    context = {
        'latest_category_list': latest_category_list,
    }
    return render(request, 'catalog/category_list.html', context)


def detail(request, pk):
    description = BoardGames.objects.get(id=pk).game_description
    context = {
        'description': description,
    }
    return render(request, 'catalog/detail.html', context)
