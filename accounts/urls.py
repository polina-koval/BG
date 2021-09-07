from django.urls import path
from accounts.views import SignUpView, ProfileListView, EditProfile, PasswordsChangeView, AdditionalEditProfile

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('dashboard/', ProfileListView.as_view(), name='view_profile'),
    path('dashboard/edit', EditProfile.as_view(), name='edit_profile'),
    path('dashboard/additional_edit', AdditionalEditProfile.as_view(), name='additional_edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
]
