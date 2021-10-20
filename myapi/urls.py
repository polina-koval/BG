from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from myapi import views as myapiviews

router = routers.DefaultRouter()
router.register(r"all_category", myapiviews.CategoryGamesViewSet)
router.register(r"all_games", myapiviews.BoardGamesViewSet)
router.register(r"all_users", myapiviews.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls",
                              namespace="rest_framework")),
]

urlpatterns += [path("api-token-auth/", views.obtain_auth_token)]
