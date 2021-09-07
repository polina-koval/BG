from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect(reverse('catalog:category_list'))
    else:
        user_form = RegistrationForm()
        args = {'user_form': user_form}
        return render(request, 'accounts/signup.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        userprofile = UserProfile.objects.get(pk=pk)
    else:
        user = request.user
        userprofile = request.user.userprofile
    args = {'user': user,
            'userprofile': userprofile
            }
    return render(request, 'accounts/detail.html', args)


def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {'user_form': user_form,
                'profile_form': profile_form,
                }
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
