# Generated by Django 5.1.2 on 2024-11-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('amount_of_rooms', models.IntegerField(verbose_name='Number of Rooms')),
                ('type_of_housing', models.CharField(choices=[('apartment', 'Apartment'), ('studio', 'Studio')], default='apartment', max_length=50, verbose_name='Type of Housing')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Status')),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
            },
        ),
    ]
