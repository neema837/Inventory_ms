# Generated by Django 4.2 on 2023-05-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employdata_cmpid_product_cpaddingdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='catimage',
            field=models.FileField(blank=True, null=True, upload_to='category imgs'),
        ),
    ]
