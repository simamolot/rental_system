# from django.db import models
#
# class Apartment(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Title", null=False)
#     description = models.TextField(verbose_name="Description", null=False)
#     city = models.CharField(max_length=100, verbose_name="City", null=False)
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", null=False)
#     amount_of_rooms = models.IntegerField(verbose_name="Number of rooms", null=False)
#     type_of_housing = models.CharField(
#         max_length=50,
#         choices=[('apartment', 'Apartment'), ('studio', 'Studio')],
#         verbose_name="Type of housing",
#         default='apartment'
#     )  # Type of housing
#     is_active = models.BooleanField(default=False, verbose_name="Active status")  # Active status
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
#
#
#     class Meta:
#         verbose_name = 'Apartment'
#         verbose_name_plural = 'Apartments'
#         db_table = 'apartments'
#
#     def __str__(self):
#         return self.title

from django.conf import settings
from django.db import models

from apps.user.models import User


class Apartment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title", null=False)
    description = models.TextField(verbose_name="Description", null=False)
    city = models.CharField(max_length=100, verbose_name="City", null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", null=False)
    amount_of_rooms = models.IntegerField(verbose_name="Number of Rooms", null=False)
    type_of_housing = models.CharField(
        max_length=50,
        choices=[('apartment', 'Apartment'), ('studio', 'Studio')],
        verbose_name="Type of Housing",
        default='apartment'
    )
    landlord = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="apartments",
        verbose_name="Landlord",
    )
    is_active = models.BooleanField(default=True, verbose_name="Active Status")

    class Meta:
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'

    def __str__(self):
        return self.title





