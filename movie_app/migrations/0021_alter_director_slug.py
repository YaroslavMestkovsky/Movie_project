# Generated by Django 4.0.3 on 2022-03-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0020_director_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
