# Generated by Django 3.2.7 on 2023-01-07 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_bookings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookings',
            new_name='Booking',
        ),
    ]
