# Generated by Django 4.0.3 on 2022-03-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0017_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie_app.actor'),
        ),
    ]
