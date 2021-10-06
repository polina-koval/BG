from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile

from django.core.mail import send_mail

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            send_mail(
                'Your registration in BG',
                'Congratulation! Have a good board game experience!',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "id")


class ProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = (
            "city",
            "bio",
            "birth_date",
        )
