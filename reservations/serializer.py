from rest_framework import serializers
from django.db import transaction
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'seat', 'session', 'user']

    @transaction.atomic
    def create(self, validated_data):
        seat = Seat.objects.select_for_update().get(id=validated_data['seat'].id)

        if seat.status != 'AVAILABLE':
            raise serializers.ValidationError('Seat is not available')

        seat.status = 'RESERVED'
        seat.save()

        return Reservation.objects.create(**validated_data)