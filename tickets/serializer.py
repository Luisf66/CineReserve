from django.utils import timezone
from rest_framework import serializers

from .models import Ticket
from reservations.models import Reservation
from reservations.serializer import ReservationSerializer


class TicketSerializer(serializers.ModelSerializer):
    reservation = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all(), 
        write_only=True
    )

    reservation_data = ReservationSerializer(
        source='reservation',
        read_only=True
    )
    
    class Meta:
        model = Ticket
        fields = ['id', 'reservation', 'reservation_data']

    def create(self, validated_data):
        reservation = validated_data['reservation']
        now = timezone.now()

        # 🔒 valida reserva
        if reservation.status != 'reserved':
            raise serializers.ValidationError("Reserva inválida.")

        if reservation.locked_until <= now:
            reservation.status = 'expired'
            reservation.save()
            raise serializers.ValidationError("Reserva expirada.")

        # 💰 confirma compra
        reservation.status = 'purchased'
        reservation.save()

        # 🎟 cria ticket
        ticket = Ticket.objects.create(reservation=reservation)

        return ticket