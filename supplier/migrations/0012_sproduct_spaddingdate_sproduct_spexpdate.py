# Generated by Django 4.2 on 2023-05-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0011_alter_sproduct_sprodimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sproduct',
            name='spaddingdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sproduct',
            name='spexpdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
