from django.urls import path
from . import views


app_name = 'tickets'

urlpatterns = [
    path('tickets/', views.TicketListCreateView.as_view(), name='ticket'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
]