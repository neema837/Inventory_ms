# Generated by Django 4.2 on 2023-05-15 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0009_suppliers_reject'),
    ]

    operations = [
        migrations.CreateModel(
            name='SproductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=20)),
                ('supid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='Sproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprodname', models.CharField(max_length=20)),
                ('sproddesc', models.CharField(max_length=50)),
                ('sprodbrand', models.CharField(blank=True, max_length=20, null=True)),
                ('sprodprice', models.BigIntegerField(blank=True, null=True)),
                ('sprodminqty', models.BigIntegerField(blank=True, null=True)),
                ('sprodmaxqty', models.BigIntegerField(blank=True, null=True)),
                ('sprodstock', models.BigIntegerField(blank=True, null=True)),
                ('sprodimage', models.FileField(upload_to='product imgs')),
                ('sprodcat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.sproductcategory')),
                ('supid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.suppliers')),
            ],
        ),
    ]
