# Generated by Django 3.0.6 on 2023-10-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unstop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seat_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_count_remaining',
            field=models.IntegerField(),
        ),
    ]
