# Generated by Django 3.0.6 on 2023-10-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_count', models.IntegerField(max_length=10)),
                ('seat_count_remaining', models.IntegerField(max_length=10)),
            ],
        ),
    ]
