from django.urls import path
from . import views  

urlpatterns = [
    path('movies/', views.MovieListAPI.as_view(), name='api_movie_list'),
    path('halls/', views.HallListAPI.as_view(), name='api_hall_list'),
   
]
