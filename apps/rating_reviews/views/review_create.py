
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied
from apps.rating_reviews.models.review import Review
from apps.rating_reviews.serializers.review_serializer import ReviewSerializer
from apps.reservations.models.reservations_model import Reservation

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        apartment = serializer.validated_data.get('apartment')

        if not Reservation.objects.filter(user=self.request.user, apartment_id=apartment).exists():
            raise PermissionDenied("Вы можете оставить отзыв только на те апартаменты, которые бронировали.")

        serializer.save(renter=self.request.user)


