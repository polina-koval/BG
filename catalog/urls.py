from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.category_list, name='category_list'),
    # ex: /catalog/category/5/
    path('category/<int:category_id>/', views.game_list, name='game_list'),
    # ex: /catalog/category/5/detail
    path('description/<pk>/', views.detail, name='detail'),

]
