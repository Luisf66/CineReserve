from django.urls import path
from . import views


app_name = 'tickets'

urlpatterns = [
    #path('tickets/', views.TicketCreateView.as_view(), name='ticket-create'),
    #path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
]