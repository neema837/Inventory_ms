# Generated by Django 4.2 on 2023-04-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admindata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adname', models.CharField(max_length=20)),
                ('admailid', models.EmailField(max_length=254)),
                ('adpwd', models.CharField(max_length=50)),
            ],
        ),
    ]
