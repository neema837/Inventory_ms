# Generated by Django 4.2 on 2023-05-23 08:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_productcategory_catimage'),
        ('imsuser', '0010_alter_cart_status_alter_customers_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addingtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
                ('prodid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.product')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsuser.customers')),
            ],
        ),
    ]
