from rest_framework.permissions import AllowAny
from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .serializer import MovieSerializer
from .models import Movie


# Create your views here.
@extend_schema(tags=['Movies'])
class MoviesListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny] # trocar para IsAuthenticated

@extend_schema(tags=['Movies'])
class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny] # trocar para IsAuthenticated