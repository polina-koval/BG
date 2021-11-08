from django.db.models import Avg, Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from catalog.forms import CommentForm
from catalog.models import BoardGames, Category, Comment


class GameListView(DetailView):
    model = Category
    template_name = "catalog/game_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = BoardGames.objects.filter(
            category=self.kwargs.get("pk"),
            status=BoardGames.StatusChoices.PUBLISHED,
        )
        return context


class CheapGameListView(ListView):
    queryset = BoardGames.cheap_games.filter(
        status=BoardGames.StatusChoices.PUBLISHED
    )
    context_object_name = "games"
    template_name = "catalog/cheap_game.html"


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_category"] = Category.objects.all()
        context["cheap_games"] = BoardGames.cheap_games.filter(
            status=BoardGames.StatusChoices.PUBLISHED
        )
        context["games_amount"] = Category.objects.filter(
            boardgames__status=BoardGames.StatusChoices.PUBLISHED
        )
        context["average_price"] = BoardGames.objects.filter(
            status=BoardGames.StatusChoices.PUBLISHED
        ).aggregate(Avg("price"))
        return context


class DetailViewGame(DetailView):
    model = BoardGames
    context_object_name = "game"
    template_name = "catalog/detail.html"


class SearchResultsView(ListView):
    model = BoardGames
    template_name = "catalog/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = BoardGames.objects.filter(
            (Q(name__icontains=query) | Q(description__icontains=query)),
            status=BoardGames.StatusChoices.PUBLISHED,
        )
        return object_list


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "catalog/add_comment.html"
    success_url = reverse_lazy("catalog:category_list")

    def form_valid(self, form):
        form.instance.game_id = self.kwargs["pk"]
        form.instance.owner = self.request.user.userprofile
        return super().form_valid(form)


def like_view(request, pk):
    game = get_object_or_404(BoardGames, id=pk)
    if game.likes.filter(id=request.user.id).exists():
        game.likes.remove(request.user)
    else:
        game.likes.add(request.user)
    return HttpResponseRedirect(reverse("catalog:detail", args=[str(pk)]))
