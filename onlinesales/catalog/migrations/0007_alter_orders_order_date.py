# Generated by Django 5.0.4 on 2024-04-18 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_orders_due_date_alter_orders_ship_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.ForeignKey(blank=True, help_text='Select order date', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='orders_order_date', to='catalog.date'),
        ),
    ]
