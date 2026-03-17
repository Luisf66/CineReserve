from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reservations/', views.ReservationListCreateView.as_view(), name='reservation'),
    path('reservations/<int:pk>/', views.ReservationRetrieveView.as_view(), name='reservation-detail'),
    path('reservations/<int:pk>/cancel/', views.CancelReservationView.as_view(), name='reservation-cancel'),
]