from django.urls import path

from accounts.views import (EditProfile,
                            LikedGameListView, PasswordsChangeView,
                            ProfileListView, SignUpView)

app_name = "accounts"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="register"),
    path("dashboard/", ProfileListView.as_view(), name="view_profile"),
    path("dashboard/edit", EditProfile.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(), name="change_password"),
    path("dashboard/<id>/likes_games", LikedGameListView.as_view(), name="liked_games"),
]
