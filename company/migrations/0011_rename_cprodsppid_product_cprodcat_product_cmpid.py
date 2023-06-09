# Generated by Django 4.2 on 2023-05-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_product_cprodsppid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cprodsppid',
            new_name='cprodcat',
        ),
        migrations.AddField(
            model_name='product',
            name='cmpid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companies'),
        ),
    ]
