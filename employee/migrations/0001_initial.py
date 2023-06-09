# Generated by Django 4.2 on 2023-05-10 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0013_remove_productcategory_cmpid_delete_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=20)),
                ('cmpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cprodname', models.CharField(max_length=20)),
                ('cproddesc', models.CharField(max_length=50)),
                ('cprodbrand', models.CharField(blank=True, max_length=20, null=True)),
                ('cprodprice', models.BigIntegerField(blank=True, null=True)),
                ('cprodminqty', models.BigIntegerField(blank=True, null=True)),
                ('cprodmaxqty', models.BigIntegerField(blank=True, null=True)),
                ('cprodstock', models.BigIntegerField(blank=True, null=True)),
                ('cprodimage', models.FileField(upload_to='product imgs')),
                ('cmpid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companies')),
                ('cprodcat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.productcategory')),
            ],
        ),
    ]
