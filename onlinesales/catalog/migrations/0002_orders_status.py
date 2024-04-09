# Generated by Django 4.2.10 on 2024-04-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Processing'), ('s', 'Shipped'), ('d', 'Delivered')], default='p', help_text='Order Status', max_length=1),
        ),
    ]
