# Generated by Django 4.2 on 2023-04-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0003_customers_uimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='uimage',
            field=models.FileField(upload_to='users'),
        ),
    ]
