# Generated by Django 3.0.6 on 2023-10-08 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unstop', '0002_auto_20231008_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='seat_count',
            new_name='booked_seat_count',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='seat_count_remaining',
            new_name='remaining_seats',
        ),
    ]
