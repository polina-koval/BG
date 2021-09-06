from django.shortcuts import render

from catalog.models import BoardGames, Category
from django.views.generic import ListView
from django.db.models import Q


def game_list(request, category_id):
    games = BoardGames.objects.filter(category=category_id)
    context = {
        'games': games,
    }
    return render(request, 'catalog/game_list.html', context)


def category_list(request):
    all_category = Category.objects.all()
    context = {
        'all_category': all_category,
    }
    return render(request, 'catalog/category_list.html', context)


def detail(request, pk):
    game = BoardGames.objects.get(id=pk)
    context = {
        'game': game,
    }
    return render(request, 'catalog/detail.html', context)


class SearchResultsView(ListView):
    model = BoardGames
    template_name = 'catalog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = BoardGames.objects.filter(Q(name_of_game__icontains=query) | Q(game_description__icontains=query))
        return object_list
