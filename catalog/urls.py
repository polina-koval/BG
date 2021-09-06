from django.urls import path

from catalog import views
from catalog.views import SearchResultsView

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.category_list, name='category_list'),
    # ex: /catalog/category/5/
    path('category/<int:category_id>/', views.game_list, name='game_list'),
    # ex: /catalog/category/5/detail
    path('description/<pk>/', views.detail, name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
