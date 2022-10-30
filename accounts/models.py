import uuid

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.template.loader import render_to_string
from weasyprint import HTML


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


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    games = models.ManyToManyField("catalog.BoardGames")

    def __str__(self):
        return f"{self.user} cart"


class Receipt(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    document = models.FileField(upload_to="checks/", blank=True, null=True)
    unique_number = models.CharField(
        primary_key=True, default=uuid.uuid4(), max_length=50, editable=False
    )

    def save(self, *args, **kwargs):
        if not self.document:
            doc = self.make_receipt()
            self.document.save(f"{self.unique_number}.pdf", ContentFile(doc))
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.unique_number)

    def make_receipt(self):
        html_string = render_to_string(
            "accounts/receipt.html",
        )
        doc = HTML(string=html_string).write_pdf()
        return doc
