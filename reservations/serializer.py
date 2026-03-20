from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from django.db import transaction

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'session', 'seat_number', 'status', 'locked_until']
        read_only_fields = ['status', 'locked_until']

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data['user']
        session = validated_data['session']
        seat_number = validated_data['seat_number']

        now = timezone.now()

        existing = Reservation.objects.filter(
            session=session,
            seat_number=seat_number,
            status='reserved',
            locked_until__gt=now
        ).first()

        if existing:
            raise serializers.ValidationError("Assento já está reservado.")

        Reservation.objects.filter(
            session=session,
            seat_number=seat_number,
            locked_until__lte=now,
            status='reserved'
        ).update(status='expired')

        # ⏱ cria nova reserva (10 minutos)
        reservation = Reservation.objects.create(
            user=user,
            session=session,
            seat_number=seat_number,
            status='reserved',
            locked_until=now + timedelta(minutes=10)
        )

        return reservation