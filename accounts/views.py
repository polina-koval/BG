from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from accounts.forms import EditProfileForm, ProfileForm, RegistrationForm


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("catalog:category_list")
    template_name = "accounts/signup.html"


class ProfileListView(ListView):
    model = User
    template_name = "accounts/detail.html"

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs.get("id"))
        return user


class EditProfile(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy("accounts:view_profile")
    template_name = "accounts/edit_profile.html"

    def get_object(self):
        return self.request.user


class AdditionalEditProfile(generic.UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:view_profile")
    template_name = "accounts/additional_edit_profile.html"

    def get_object(self):
        return self.request.user.userprofile


class PasswordsChangeView(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy("accounts:view_profile")
    template_name = "accounts/change_password.html"


class LikedGameListView(ListView):
    model = User
    template_name = "accounts/like_game_list_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = User.objects.get(id=self.kwargs.get("id")).game_likes.all()
        return context
