# Generated by Django 4.2.1 on 2023-06-05 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0020_alter_order_orderdate_alter_wishlist_waddingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateField(default=datetime.date(2023, 6, 5)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='waddingdate',
            field=models.DateField(default=datetime.date(2023, 6, 5)),
        ),
    ]
