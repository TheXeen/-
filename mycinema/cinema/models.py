from django.db import models
from django.utils import timezone

# Модель для кинотеатра (зал)
class Hall(models.Model):
    name = models.CharField(max_length=100)  # Имя зала
    size = models.PositiveIntegerField()  # Количество мест

    def __str__(self):
        return self.name

# Модель для фильмов
class Movie(models.Model):
    title = models.CharField(max_length=100)  # Название фильма
    description = models.TextField()  # Описание фильма
    release_date = models.DateField()  # Дата выхода
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)  # Постер

    def __str__(self):
        return self.title

# Модель для сеансов
class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Сеанс связан с фильмом
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)  # Сеанс проходит в определенном зале
    start_time = models.DateTimeField()  # Время начала сеанса
    end_time = models.DateTimeField()  # Время окончания сеанса
    date = models.DateField()  # Дата показа сеанса
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена билета на сеанс

    def __str__(self):
        return f"{self.movie.title} in {self.hall.name} on {self.date}"



