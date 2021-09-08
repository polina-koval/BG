from catalog.models import BoardGames, Category, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from catalog.forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


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


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'catalog/add_comment.html'
    success_url = reverse_lazy('catalog:category_list')

    def form_valid(self, form):
        form.instance.game_id = self.kwargs['pk']
        return super().form_valid(form)


def like_view(request, pk):
    game = get_object_or_404(BoardGames, id=request.POST.get('game_id'))
    liked = False
    if game.likes.filter(id=request.user.id).exists():
        game.likes.remove(request.user)
        liked = False
    else:
        game.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('catalog:detail', args=[str(pk)]))