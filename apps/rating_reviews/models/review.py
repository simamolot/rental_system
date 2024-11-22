from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


from apps.apartments.models.apartments import Apartment
from apps.user.models import User


class Review(models.Model):
    renter = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='reviews', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


