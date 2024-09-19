from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Главная страница
    path('movies/', views.MovieListView.as_view(), name='movie_list'),  # Страница со списком фильмов
    
    # Пути для REST API
    path('api/movies/', views.MovieListAPI.as_view(), name='movie_list_api'),  # API для списка фильмов
    path('api/movies/<int:pk>/', views.MovieDetailAPI.as_view(), name='movie_detail_api'),  # API для детальной информации о фильме
    
    # API для создания залов
    path('api/halls/', views.HallCreateAPI.as_view(), name='hall_create_api'),
    
    # API для создания сеансов
    path('api/sessions/', views.SessionCreateAPI.as_view(), name='session_create_api'),
    
    # Страница со списком залов
    path('halls/', views.HallListView.as_view(), name='hall_list'),
    
    # Страница со списком сеансов
    path('sessions/', views.SessionListView.as_view(), name='session_list'),

    # Страница для покупки билетов
    path('tickets/', views.TicketView.as_view(), name='ticket_list'),
    
    path('halls/', views.HallListView.as_view(), name='api_hall_list'),
]
