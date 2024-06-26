# Generated by Django 5.0.4 on 2024-04-18 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_orders_sales_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='sales_order_line_number',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Enter sales order line number', null=True),
        ),
    ]
