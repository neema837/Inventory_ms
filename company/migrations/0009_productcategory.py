# Generated by Django 4.2 on 2023-05-04 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_product_cprodbrand'),
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
    ]