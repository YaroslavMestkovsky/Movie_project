from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

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

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
