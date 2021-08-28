from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns =  [
    # ex: /catalog/
    path('', views.category_list, name='category_list'),
    # ex: /category/catalog/5/
    path('<int:category_id>/', views.game_list, name='game_list'),
    # ex: /category/catalog/5/detail
    path('<int:category_id>/<pk>/', views.detail, name='detail'),

]