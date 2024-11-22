from django.db.models import Avg
from rest_framework import serializers
from apps.apartments.models.apartments import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = ['title', 'description', 'city', 'price', 'amount_of_rooms', 'type_of_housing', 'is_active', 'average_rating']  # Добавили 'average_rating'
        read_only_fields = ['average_rating']  # Исправили read_only_field на read_only_fields

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(average, 1) if average is not None else None

# from django.db.models import Avg
# from rest_framework import serializers
# from apps.apartments.models.apartments import Apartment
#
# class ApartmentSerializer(serializers.ModelSerializer):
#     average_rating = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Apartment
#         fields = ['title', 'description', 'city', 'price', 'amount_of_rooms', 'type_of_housing', 'is_active', 'average_rating']
#         read_only_fields = ['average_rating']
#
#     def get_average_rating(self, obj):
#         average = obj.reviews.aggregate(Avg('rating'))['rating__avg']
#         return round(average, 1) if average is not None else None

