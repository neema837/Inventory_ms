# Generated by Django 4.2 on 2023-04-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_alter_suppliers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='splic',
            field=models.FileField(upload_to='slicense'),
        ),
    ]