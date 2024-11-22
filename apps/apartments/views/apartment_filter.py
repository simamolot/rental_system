# import django_filters
#
# from ..models.apartments import Apartment
#
# class ApartmentFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
#     description = django_filters.CharFilter(field_name='description',lookup_expr='icontains')
#     min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
#     min_rooms = django_filters.NumberFilter(field_name="count_room", lookup_expr='gte')
#     max_rooms = django_filters.NumberFilter(field_name="count_room", lookup_expr='lte')
#     type_of_housing = django_filters.CharFilter(field_name="type_of_housing", lookup_expr='icontains')
#
#     class Meta:
#         model = Apartment
#         fields = ['title', 'description']

import django_filters
from django.forms import TextInput, NumberInput
from ..models.apartments import Apartment

class ApartmentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title contains:',
        widget=TextInput(attrs={'placeholder': 'Enter title...', 'class': 'form-control'})
    )
    description = django_filters.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        label='Description contains:',
        widget=TextInput(attrs={'placeholder': 'Enter description...', 'class': 'form-control'})
    )
    min_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr='gte',
        label='Price (min):',
        widget=NumberInput(attrs={'placeholder': 'Min price...', 'class': 'form-control'})
    )
    max_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr='lte',
        label='Price (max):',
        widget=NumberInput(attrs={'placeholder': 'Max price...', 'class': 'form-control'})
    )
    min_rooms = django_filters.NumberFilter(
        field_name="amount_of_rooms",
        lookup_expr='gte',
        label='Rooms (min):',
        widget=NumberInput(attrs={'placeholder': 'Min rooms...', 'class': 'form-control'})
    )
    max_rooms = django_filters.NumberFilter(
        field_name="amount_of_rooms",
        lookup_expr='lte',
        label='Rooms (max):',
        widget=NumberInput(attrs={'placeholder': 'Max rooms...', 'class': 'form-control'})
    )
    type_of_housing = django_filters.CharFilter(
        field_name="type_of_housing",
        lookup_expr='icontains',
        label='Type of housing:',
        widget=TextInput(attrs={'placeholder': 'e.g. Apartment, Studio...', 'class': 'form-control'})
    )

    class Meta:
        model = Apartment
        fields = ['title', 'description', 'min_price', 'max_price', 'min_rooms', 'max_rooms', 'type_of_housing']
