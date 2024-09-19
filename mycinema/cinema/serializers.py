from rest_framework import serializers
from .models import Movie, Hall, Session

# Сериализатор для модели фильмов
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'poster']

# Сериализатор для модели залов
class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name', 'size']  # Используйте 'size', если это правильное поле

# Сериализатор для модели сеансов
class SessionSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    hall = serializers.PrimaryKeyRelatedField(queryset=Hall.objects.all())

    class Meta:
        model = Session
        fields = ['id', 'movie', 'hall', 'start_time', 'end_time', 'date', 'price']
