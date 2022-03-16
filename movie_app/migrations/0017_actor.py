# Generated by Django 4.0.3 on 2022-03-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_alter_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Не известно', max_length=50)),
                ('last_name', models.CharField(default='Не известно', max_length=50)),
                ('gender', models.CharField(choices=[('WOM', 'Wooman'), ('MAN', 'Man'), ('NON', 'Не известно')], default='NON', max_length=3)),
            ],
        ),
    ]
