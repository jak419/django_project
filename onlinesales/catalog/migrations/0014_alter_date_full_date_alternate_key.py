# Generated by Django 5.0.4 on 2024-04-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_date_calendar_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='full_date_alternate_key',
            field=models.DateField(),
        ),
    ]
