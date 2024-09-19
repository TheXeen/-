from django.views.generic import TemplateView, ListView
from rest_framework import generics
from .models import Movie, Hall, Session
from .serializers import MovieSerializer, HallSerializer, SessionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


# Главная страница
class HomeView(TemplateView):
    template_name = 'cinema/home.html'

# Список фильмов (страница)
class MovieListView(ListView):
    model = Movie
    template_name = 'cinema/movie_list.html'
    context_object_name = 'movies'

# API для создания и получения списка фильмов
class MovieListAPI(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# API для получения, обновления и удаления конкретного фильма
class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# API для создания и получения списка залов
class HallCreateAPI(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

# API для создания и получения списка сеансов
class SessionCreateAPI(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# Список залов (страница)
class HallListView(ListView):
    model = Hall
    template_name = 'cinema/hall_list.html'
    context_object_name = 'halls'

# Список сеансов (страница)
class SessionListView(ListView):
    model = Session
    template_name = 'cinema/session_list.html'
    context_object_name = 'sessions'

# Страница для билетов
class TicketView(TemplateView):
    template_name = 'cinema/tickets.html'

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()     
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)