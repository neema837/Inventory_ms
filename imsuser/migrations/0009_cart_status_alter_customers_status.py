# Generated by Django 4.2 on 2023-05-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0008_cart_delete_customercart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
