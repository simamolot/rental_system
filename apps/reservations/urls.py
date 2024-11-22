from django.urls import path

from apps.reservations.views.reservations import ReservationCreateView, ManageReservationsView, CheckReservationView


urlpatterns = [
    path('create/<int:pk>/', ReservationCreateView.as_view(), name='reservation_create'),
    path('approve/<int:pk>/', ManageReservationsView.as_view(), name='approve_reservation'),
    path('check/<int:pk>/', CheckReservationView.as_view(), name='check_reservation'),

]