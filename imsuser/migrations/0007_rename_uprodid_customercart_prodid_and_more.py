# Generated by Django 4.2 on 2023-05-22 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imsuser', '0006_alter_customercart_uprodqty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercart',
            old_name='uprodid',
            new_name='prodid',
        ),
        migrations.RenameField(
            model_name='customercart',
            old_name='userid',
            new_name='uid',
        ),
    ]
