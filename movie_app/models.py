from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from pytils.translit import slugify


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=50, default='Не известно')
    last_name = models.CharField(max_length=50, default='Не известно')
    director_mail = models.EmailField(default='Не известно')
    slug = models.SlugField(default='', null=False, blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Director, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('one_director', args=[self.slug])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'Этаж {self.floor}, номер {self.number}'


class Actor(models.Model):
    F = 'Male'
    M = 'Female'
    N = 'No data'
    GENDER_COICES = [
        (F, 'Женщина'),
        (M, 'Мужчина'),
        (N, 'Не известно')
    ]
    first_name = models.CharField(max_length=50, default='Не известно')
    last_name = models.CharField(max_length=50, default='Не известно')
    gender = models.CharField(max_length=15, choices=GENDER_COICES, default=N)
    slug = models.SlugField(default='', null=False, blank=True, allow_unicode=True)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == self.M:
            return f'Актер {self.first_name} {self.last_name}'
        elif self.gender == self.F:
            return f'Актриса {self.first_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Actor, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_actor', args=[self.slug])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_COICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    NO = 'NO'
    YE = 'YE'
    VIEWED_CHOICE = [
        (NO, 'В очереди'),
        (YE, 'Просмотрено'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    viewed = models.CharField(max_length=2, choices=VIEWED_CHOICE, default=NO)
    currency = models.CharField(max_length=3, choices=CURRENCY_COICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'

# python manage.py shell_plus --print-sql
