from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField(max_length=10, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=30, null=False, verbose_name='Last Name')
    date_birth = models.DateField(null=True, verbose_name='Date of Birth')
    email = models.EmailField(unique=True, verbose_name='Email')
    city = models.CharField(max_length=30, null=True, verbose_name='City')
    phone_code = models.CharField(max_length=30, null=True, verbose_name='Country Code')
    phone_number = models.IntegerField(
        blank=True,
        null=True,
        help_text='Enter the phone number without the country code',
        verbose_name='Phone Number',
    )
    is_landlord = models.BooleanField(default=False, verbose_name='I am a landlord')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='Groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='User Permissions',
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'date_birth', 'country', 'city', 'country_code']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

