# Generated by Django 4.2 on 2023-05-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0007_alter_suppliers_spphno'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
