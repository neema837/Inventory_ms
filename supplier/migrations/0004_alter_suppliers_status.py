# Generated by Django 4.2 on 2023-04-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_alter_suppliers_splic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
