from django.urls import path
from . import views  # Импортируйте ваши view-функции или классы

urlpatterns = [
    path('movies/', views.MovieListAPI.as_view(), name='api_movie_list'),
    path('halls/', views.HallListAPI.as_view(), name='api_hall_list'),
    # Добавьте свои другие API-маршруты здесь
]
