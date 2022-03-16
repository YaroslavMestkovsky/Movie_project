# Generated by Django 4.0.3 on 2022-03-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0023_actor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('Женщина', 'Женщина'), ('Мужчина', 'Мужчина'), ('Не известно', 'Не известно')], default='Не известно', max_length=15),
        ),
    ]
