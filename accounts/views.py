from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from accounts.forms import ProfileForm, RegistrationForm
from accounts.models import UserProfile


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("accounts:edit_profile")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy("accounts:edit_profile"))


class ProfileListView(ListView):
    model = User
    template_name = "accounts/detail.html"

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs.get("id"))
        return user


class EditProfile(generic.UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:view_profile")
    template_name = "accounts/edit_profile.html"

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
        context["games"] = User.objects.get(
            id=self.kwargs.get("id")).game_likes.all()
        return context


class CommentsFromUser(ListView):
    model = UserProfile
    template_name = "accounts/comment_from_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = (
            UserProfile.objects.get(id=self.kwargs.get("id"))
            .comment_set.all()
            .order_by("-date_added")
        )
        return context
