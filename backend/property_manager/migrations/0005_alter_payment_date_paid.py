# Generated by Django 4.2.15 on 2024-08-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_manager', '0004_property_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_paid',
            field=models.DateTimeField(),
        ),
    ]
