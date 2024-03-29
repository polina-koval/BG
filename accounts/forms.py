from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from dotenv import load_dotenv

from accounts.models import UserProfile

load_dotenv()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            send_mail(
                "Your registration in BG",
                "Congratulation! Have a good board game experience!",
                "BG Administrator <no-reply@bg.com>",
                [user.email]
            )
            user.save()

        return user


class ProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = (
            "name",
            "email",
            "username",
            "city",
            "bio",
            "birth_date",
        )
