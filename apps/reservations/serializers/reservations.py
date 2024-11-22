from rest_framework import serializers

from apps.reservations.models.reservations_model import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id','start_reservations', 'end_reservations', 'comment']
