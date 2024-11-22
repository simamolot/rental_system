from rest_framework import serializers
from apps.reservations.models.reservations_model import Reservation

class ApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user', 'canceled', 'approved']
        read_only_fields = ['start_reservations', 'end_reservations']

    def update(self, instance, validated_data):
        instance.canceled = validated_data.get('canceled', instance.canceled)
        instance.approved = validated_data.get('approved', instance.approved)
        instance.save()
        return instance



