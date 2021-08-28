# Generated by Django 3.2.6 on 2021-08-28 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Without category', max_length=200)),
            ],
            options={
                'verbose_name': 'Category name',
                'verbose_name_plural': 'Category names',
            },
        ),
        migrations.CreateModel(
            name='BoardGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_game', models.CharField(max_length=200)),
                ('start_player_age', models.IntegerField(default=0)),
                ('rating_from_the_store', models.IntegerField(default=0)),
                ('category_text', models.CharField(default='For all', max_length=200)),
                ('game_description', models.TextField(default="Let's add later")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'Board Game',
                'verbose_name_plural': 'Board Games',
            },
        ),
    ]
