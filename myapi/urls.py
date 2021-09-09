from django.urls import include, path
from rest_framework import routers

from myapi import views

router = routers.DefaultRouter()
router.register(r"all_category", views.CategoryGamesViewSet)
router.register(r"all_games", views.BoardGamesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
