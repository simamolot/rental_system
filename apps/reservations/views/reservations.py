
from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.apartments.models.apartments import Apartment
from apps.reservations.models.reservations_model import Reservation
from apps.reservations.serializers.approve import ApproveSerializer
# from apps.reservations.serializers.cancel_serializers import CancelSerializer
from apps.reservations.serializers.reservations import ReservationSerializer
from apps.user.permissions.landlord_permissions import IsLandlordOwner


# Create your views here.
class ReservationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        apartment_id = self.kwargs.get('pk')
        try:
            apartment = Apartment.objects.get(pk=apartment_id)
        except Apartment.DoesNotExist:
            raise NotFound('Announcement not found.')


        serializer.save(user=self.request.user, apartment=apartment, approved=False)


class CheckReservationView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Reservation.objects.filter(user=user, canceled=False)  # Фильтруем не отмененные бронирования
        return Reservation.objects.none()


# class CancelReservationView(generics.UpdateAPIView):
#     serializer_class = CancelSerializer
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         return Reservation.objects.filter(user=self.request.user)
#
#     def perform_update(self, serializer):
#         reservation_id = self.kwargs.get('pk')
#         try:
#             reservation = Reservation.objects.get(pk=reservation_id, user=self.request.user)
#         except Reservation.DoesNotExist:
#             raise NotFound('Reservation not found.')
#
#         reservation.cancel()
#         serializer.save()



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from apps.apartments.models.apartments import Apartment
from apps.reservations.models.reservations_model import Reservation
from apps.user.permissions.landlord_permissions import IsLandlordOwner

class ManageReservationsView(APIView):
    permission_classes = [IsLandlordOwner]

    def get(self, request, pk):
        try:
            apartment = Apartment.objects.get(pk=pk)
        except Apartment.DoesNotExist:
            raise NotFound("Apartment not found.")

        reservations = Reservation.objects.filter(apartment=apartment)
        if not reservations.exists():
            raise NotFound("No reservations found for this apartment.")

        data = [
            {
                "reservation_id": reservation.id,
                "user_id": reservation.user.id,
                "user_name": reservation.user.username,
                'start_reservations': reservation.start_reservations,
                'end_reservations': reservation.end_reservations,
                "approved": reservation.approved,
                "canceled": reservation.canceled,
            }
            for reservation in reservations
        ]
        return Response(data)

    def put(self, request, pk):
        reservation_id = request.data.get("reservation_id")
        action = request.data.get("action")

        if not reservation_id or not action:
            raise ValidationError("Both 'reservation_id' and 'action' are required.")

        if action not in ["approve", "cancel"]:
            raise ValidationError("Invalid action. Use 'approve' or 'cancel'.")

        try:
            reservation = Reservation.objects.get(pk=reservation_id, apartment_id=pk)
        except Reservation.DoesNotExist:
            raise NotFound("Reservation not found for this apartment.")

        if action == "approve":
            reservation.approved = True
            reservation.save()
            return Response({"message": "Reservation approved."})
        elif action == "cancel":
            reservation.canceled = True
            reservation.save()
            return Response({"message": "Reservation canceled."})
