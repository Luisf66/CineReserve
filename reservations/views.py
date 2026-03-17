from rest_framework import generics
from .serializer import ReservationSerializer

# Create your views here.
class ReservationCreateView(generics.CreateAPIView):
    serializer_class = None