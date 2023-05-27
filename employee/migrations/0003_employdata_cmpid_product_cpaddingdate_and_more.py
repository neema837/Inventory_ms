# Generated by Django 4.2 on 2023-05-16 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_remove_productcategory_cmpid_delete_product_and_more'),
        ('employee', '0002_employdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='employdata',
            name='cmpid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companies'),
        ),
        migrations.AddField(
            model_name='product',
            name='cpaddingdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cpexpdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]