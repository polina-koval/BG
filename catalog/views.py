from django.shortcuts import render
# from django.views import generic

from catalog.models import BoardGames, Category


# class GameList(generic.ListView):
#    template_name = 'catalog/game_list.html'
#    context_object_name = 'games'
#
#    def get_queryset(self):
#        """Return the game."""
#        return BoardGames.objects.filter(category=category_id)

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
