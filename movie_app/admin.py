from django.contrib import admin, messages
from django.contrib.auth.models import User
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<70', 'Низкий'),
            ('от 70 до 85', 'Средний'),
            ('от 85', 'Высокий'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<70':
            return queryset.filter(rating__lt=70)
        elif self.value() == 'от 70 до 85':
            return queryset.filter(rating__gte=70).filter(rating__lt=85)
        elif self.value() == 'от 85':
            return queryset.filter(rating__gte=85)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # exclude = ['slug'] # поле, которое не отображается при регистрации нового фильма
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'director', 'viewed', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'currency', 'viewed', 'director']
    filter_horizontal = ['actors']
    # ordering = ['rating'] # сортировка по тегу рейтинг
    list_per_page = 10
    actions = ['set_dollars', 'set_euros']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 70:
            return 'Фильм не очень'
        elif 70 <= movie.rating < 85:
            return 'Можно смотреть'
        elif movie.rating >= 85:
            return 'Топ, обязательно к просмотру'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Записей обновлено: {count_updated}',
        )

    @admin.action(description='Установить валюту в евро')
    def set_euros(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Записей обновлено: {count_updated}',
        )
