# Generated by Django 4.2.1 on 2023-05-31 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0014_order_cartid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='addingtime',
            field=models.DateField(default=datetime.date(2023, 5, 31)),
        ),
    ]
