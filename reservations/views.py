from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from drf_spectacular.utils import extend_schema

from .serializer import ReservationSerializer
from .models import Reservation

# Create your views here.
@extend_schema(tags=["Reservations"])
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema(tags=["Reservations"])
class ReservationRetrieveView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@extend_schema(tags=["Reservations"])
class CancelReservationView(APIView):

    def post(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response(
                {"detail": "Reserva não encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )

        now = timezone.now()

        if reservation.status != 'reserved':
            return Response(
                {"detail": "Reserva não está ativa."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if reservation.locked_until <= now:
            reservation.status = 'expired'
            reservation.save()

            return Response(
                {"detail": "Reserva já estava expirada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        reservation.status = 'expired'
        reservation.save()

        return Response(
            {"detail": "Reserva cancelada com sucesso."},
            status=status.HTTP_200_OK
        )