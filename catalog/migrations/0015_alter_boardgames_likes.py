# Generated by Django 3.2.6 on 2021-09-13 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0014_rename_game_description_boardgames_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgames',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='game_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]