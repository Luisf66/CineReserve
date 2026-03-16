from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.MoviesListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MoviesRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]