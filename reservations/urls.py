from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reservations/', views.ReservationCreateView.as_view(), name='reservation-create'),
    #path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    #path('reservations/<int:pk>/cancel/', views.ReservationCancelView.as_view(), name='reservation-cancel'),
]