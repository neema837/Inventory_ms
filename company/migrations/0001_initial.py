# Generated by Django 4.2 on 2023-04-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpname', models.CharField(max_length=20)),
                ('cpmail', models.EmailField(max_length=254)),
                ('cpphno', models.BigIntegerField()),
                ('cpaddr', models.CharField(max_length=30)),
                ('cpcity', models.CharField(max_length=20)),
                ('cpzip', models.CharField(max_length=20)),
                ('cpstate', models.CharField(max_length=20)),
                ('cpcountry', models.CharField(max_length=20)),
                ('cptype', models.CharField(max_length=20)),
                ('cplic', models.FileField(upload_to='clicense')),
                ('cppwd', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]