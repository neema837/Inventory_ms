# Generated by Django 4.2 on 2023-04-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='splic',
            field=models.FileField(upload_to=''),
        ),
    ]
