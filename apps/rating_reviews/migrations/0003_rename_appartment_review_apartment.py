# Generated by Django 5.1.2 on 2024-11-21 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating_reviews', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='appartment',
            new_name='apartment',
        ),
    ]
