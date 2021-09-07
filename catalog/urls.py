from django.urls import path

from catalog import views
from catalog.views import SearchResultsView

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.CategoryListView.as_view(), name='category_list'),
    # ex: /catalog/category/5/
    path('category/<pk>/', views.GameListView.as_view(), name='game_list'),
    # ex: /catalog/category/5/detail
    path('description/<pk>/', views.DetailViewGame.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('description/<pk>/comment', views.AddCommentView.as_view(), name='add_comment'),
]
