# Generated by Django 5.0.6 on 2024-11-08 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetailaddress',
            name='kebele',
        ),
    ]