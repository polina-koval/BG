from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def update_user(sender, instance, created, **kwargs):
    userprofile = instance
    user = userprofile.user

    if not created:
        user.first_name = userprofile.name
        user.username = userprofile.username
        user.email = userprofile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=UserProfile)
post_delete.connect(delete_user, sender=UserProfile)
