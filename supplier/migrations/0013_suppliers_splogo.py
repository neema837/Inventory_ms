# Generated by Django 4.2.1 on 2023-06-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0012_sproduct_spaddingdate_sproduct_spexpdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers',
            name='splogo',
            field=models.FileField(blank=True, null=True, upload_to='slogo'),
        ),
    ]
