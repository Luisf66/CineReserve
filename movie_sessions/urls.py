from django.urls import path
from . import views


app_name = 'movie_sessions'

urlpatterns = [
    path('sessions/', views.SessionListCreateView.as_view(), name='session-list-create'),
    path('sessions/<int:pk>/', views.SessionRetrieveUpdateDestroyView.as_view(), name='session-detail'),

    path('movies/<int:movie_id>/sessions/', views.MovieSessionsListView.as_view(), name='movie-sessions'),
    #path('sessions/<int:pk>/seats/', views.SeatMapView.as_view(), name='session-seat-map'),
]