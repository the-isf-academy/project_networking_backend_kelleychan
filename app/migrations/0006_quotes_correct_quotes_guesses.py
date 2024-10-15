# Generated by Django 5.1.2 on 2024-10-15 07:26

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_quotes_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='correct',
            field=banjo.models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotes',
            name='guesses',
            field=banjo.models.IntegerField(default=0),
        ),
    ]
