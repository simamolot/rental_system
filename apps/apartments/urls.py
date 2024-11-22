from django.urls import path

from .models.apartments import Apartment
from .views.apartment_create import ApartmentCreateAPI, ApartmentDetailAPI, ApartmentSearch, ApartmentUpdateDeleteAPI

urlpatterns =[
    path('', ApartmentSearch.as_view()),
    path('create/', ApartmentCreateAPI.as_view()),
    path('<int:pk>/', ApartmentDetailAPI.as_view()),
    path('update/<int:pk>/', ApartmentUpdateDeleteAPI.as_view()),
     ]