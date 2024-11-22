from django.db.models import Avg
from rest_framework import serializers

from apps.rating_reviews.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['renter', 'apartment', 'comment', 'rating']
        read_only_fields = ['renter']

