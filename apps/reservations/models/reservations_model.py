from django.db import models
from django.db.models import ForeignKey

from apps.apartments.models.apartments import Apartment
from apps.user.models import User


class Reservation(models.Model):
    user = ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    apartment = ForeignKey(Apartment, related_name='reservations', on_delete=models.CASCADE, null=True)
    start_reservations = models.DateField(verbose_name='Start date', null=False, blank=False, unique=True)
    end_reservations = models.DateField(verbose_name='End date', null=False, blank=False, unique=True)
    comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    canceled = models.BooleanField(default=False, verbose_name='Is canceled')
    approved = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        unique_together = (('user', 'start_reservations', 'end_reservations'),)

    def cancel(self):
        self.is_canceled = True
        self.save()

