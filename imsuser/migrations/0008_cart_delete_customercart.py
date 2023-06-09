# Generated by Django 4.2 on 2023-05-22 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_productcategory_catimage'),
        ('imsuser', '0007_rename_uprodid_customercart_prodid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uprodqty', models.BigIntegerField(blank=True, default=1, null=True)),
                ('addingtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('prodid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.product')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsuser.customers')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerCart',
        ),
    ]
