# Generated by Django 4.2 on 2023-05-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0005_customercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercart',
            name='uprodqty',
            field=models.BigIntegerField(blank=True, default=1, null=True),
        ),
    ]
