from django.shortcuts import render

from catalog.models import BoardGames, Category
from django.views.generic import ListView, DetailView
from django.db.models import Q


class GameListView(DetailView):
    model = Category
    template_name = 'catalog/game_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = BoardGames.objects.filter(category=self.kwargs.get('pk'))
        return context


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'all_category'
    template_name = 'catalog/category_list.html'


class DetailViewGame(DetailView):
    model = BoardGames
    context_object_name = 'game'
    template_name = 'catalog/detail.html'


class SearchResultsView(ListView):
    model = BoardGames
    template_name = 'catalog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = BoardGames.objects.filter(Q(name_of_game__icontains=query) | Q(game_description__icontains=query))
        return object_list
