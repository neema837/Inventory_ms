# Generated by Django 4.2.1 on 2023-06-05 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0017_cpurchase_orderstatus_cpurchase_paymentstatus_and_more'),
        ('employee', '0006_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='cmpid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companies'),
        ),
    ]
