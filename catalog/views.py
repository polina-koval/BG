from django.template import loader
from django.shortcuts import render

from .models import BoardGames, Category


def game_list(request, category_id):

    latest_game_list = BoardGames.objects.all()
    template = loader.get_template('catalog/game_list.html')
    context = {
        'latest_game_list': latest_game_list,
    }
    return render(request, 'catalog/game_list.html', context)

def category_list(request):
    latest_category_list = Category.objects.all()
    template = loader.get_template('catalog/category_list.html')
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
