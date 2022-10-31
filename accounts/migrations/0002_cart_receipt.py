# Generated by Django 3.2.6 on 2022-10-30 10:04
import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.ManyToManyField(to='catalog.BoardGames')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('document', models.FileField(blank=True, null=True, upload_to='checks/')),
                ('unique_number', models.CharField(default=uuid.UUID(
                    '11bd9e9b-d135-49aa-8393-2957c803f341'), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.cart')),
            ],
        ),
    ]
