from django_filters.filters import OrderingFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.views import APIView

from apps.apartments.models.apartments import Apartment
from apps.apartments.serializers.serializer_apartment import ApartmentSerializer

from apps.apartments.views.apartment_filter import ApartmentFilter
from apps.user.permissions.landlord_permissions import IsLandlord, IsLandlordOwner

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from apps.apartments.models.apartments import Apartment
from apps.apartments.serializers.serializer_apartment import ApartmentSerializer
from apps.user.permissions.landlord_permissions import IsLandlordOwner


class ApartmentCreateAPI(generics.CreateAPIView):
    permission_classes = [IsLandlord]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

class ApartmentDetailAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    lookup_field = 'pk'




class ApartmentUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsLandlordOwner]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    lookup_field = 'pk'




class ApartmentSearch(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = ApartmentFilter