# Generated by Django 5.1.1 on 2024-10-15 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logistics', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='In Transit', max_length=50)),
                ('logistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='logistics.logistic')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='orders.order')),
            ],
        ),
    ]
