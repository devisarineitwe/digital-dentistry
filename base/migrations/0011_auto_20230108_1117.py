# Generated by Django 3.2.7 on 2023-01-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20230108_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(max_length=250),
        ),
    ]
