# Generated by Django 4.2.10 on 2024-04-03 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_alternate_key', models.CharField(help_text='Enter the currency code (e.g., USD, EUR)', max_length=3, unique=True)),
                ('currency_name', models.CharField(help_text='Enter the currency name (e.g., United States Dollar, Euro)', max_length=50)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_alternate_key', models.CharField(max_length=15, unique=True)),
                ('title', models.CharField(blank=True, max_length=8, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('english_education', models.CharField(blank=True, max_length=40, null=True)),
                ('spanish_education', models.CharField(blank=True, max_length=40, null=True)),
                ('french_education', models.CharField(blank=True, max_length=40, null=True)),
                ('english_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('spanish_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('french_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('house_owner_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('number_cars_owned', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=120, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('date_first_purchase', models.DateField(blank=True, null=True)),
                ('commute_distance', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date_key', models.IntegerField(primary_key=True, serialize=False)),
                ('full_date_alternate_key', models.DateField(unique=True)),
                ('day_number_of_week', models.PositiveSmallIntegerField()),
                ('english_day_name_of_week', models.CharField(max_length=10)),
                ('spanish_day_name_of_week', models.CharField(max_length=10)),
                ('french_day_name_of_week', models.CharField(max_length=10)),
                ('day_number_of_month', models.PositiveSmallIntegerField()),
                ('day_number_of_year', models.PositiveSmallIntegerField()),
                ('week_number_of_year', models.PositiveSmallIntegerField()),
                ('english_month_name', models.CharField(max_length=10)),
                ('spanish_month_name', models.CharField(max_length=10)),
                ('french_month_name', models.CharField(max_length=10)),
                ('month_number_of_year', models.PositiveSmallIntegerField()),
                ('calendar_quarter', models.PositiveSmallIntegerField()),
                ('calendar_year', models.SmallIntegerField()),
                ('calendar_semester', models.PositiveSmallIntegerField()),
                ('fiscal_quarter', models.PositiveSmallIntegerField()),
                ('fiscal_year', models.SmallIntegerField()),
                ('fiscal_semester', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Date',
                'verbose_name_plural': 'Dates',
            },
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_subcategory_alternate_key', models.IntegerField(blank=True, help_text='Enter the product subcategory alternate key', null=True, unique=True)),
                ('english_product_subcategory_name', models.CharField(help_text='Enter the English name of the product subcategory', max_length=50)),
                ('spanish_product_subcategory_name', models.CharField(blank=True, help_text='Enter the Spanish name of the product subcategory', max_length=50, null=True)),
                ('french_product_subcategory_name', models.CharField(blank=True, help_text='Enter the French name of the product subcategory', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Product Subcategory',
                'verbose_name_plural': 'Product Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_alternate_key', models.IntegerField(blank=True, null=True, unique=True)),
                ('english_promotion_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spanish_promotion_name', models.CharField(blank=True, max_length=255, null=True)),
                ('french_promotion_name', models.CharField(blank=True, max_length=255, null=True)),
                ('discount_pct', models.FloatField(blank=True, null=True)),
                ('english_promotion_type', models.CharField(blank=True, max_length=50, null=True)),
                ('spanish_promotion_type', models.CharField(blank=True, max_length=50, null=True)),
                ('french_promotion_type', models.CharField(blank=True, max_length=50, null=True)),
                ('english_promotion_category', models.CharField(blank=True, max_length=50, null=True)),
                ('spanish_promotion_category', models.CharField(blank=True, max_length=50, null=True)),
                ('french_promotion_category', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('min_qty', models.IntegerField(blank=True, null=True)),
                ('max_qty', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_alternate_key', models.CharField(blank=True, help_text='Enter the product alternate key', max_length=25, null=True, unique=True)),
                ('weight_unit_measure_code', models.CharField(blank=True, help_text='Enter the weight unit measure code', max_length=3, null=True)),
                ('size_unit_measure_code', models.CharField(blank=True, help_text='Enter the size unit measure code', max_length=3, null=True)),
                ('english_product_name', models.CharField(help_text='Enter the English name of the product', max_length=50)),
                ('standard_cost', models.DecimalField(blank=True, decimal_places=4, help_text='Enter the standard cost of the product', max_digits=19, null=True)),
                ('finished_goods_flag', models.BooleanField(help_text='Indicate whether the product is a finished good')),
                ('color', models.CharField(help_text='Enter the color of the product', max_length=15)),
                ('safety_stock_level', models.SmallIntegerField(blank=True, help_text='Enter the safety stock level', null=True)),
                ('reorder_point', models.SmallIntegerField(blank=True, help_text='Enter the reorder point', null=True)),
                ('list_price', models.DecimalField(blank=True, decimal_places=4, help_text='Enter the list price of the product', max_digits=19, null=True)),
                ('days_to_manufacture', models.IntegerField(blank=True, help_text='Enter the number of days required to manufacture the product', null=True)),
                ('english_description', models.TextField(blank=True, help_text='Enter the English description of the product', max_length=400, null=True)),
                ('start_date', models.DateTimeField(blank=True, help_text='Enter the start date of the product availability', null=True)),
                ('end_date', models.DateTimeField(blank=True, help_text='Enter the end date of the product availability', null=True)),
                ('status', models.CharField(blank=True, help_text='Enter the status of the product', max_length=7, null=True)),
                ('product_subcategory', models.ForeignKey(blank=True, help_text='Select the product subcategory', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.productsubcategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_order_number', models.CharField(help_text='Enter sales order number', max_length=20)),
                ('sales_order_line_number', models.PositiveSmallIntegerField(help_text='Enter sales order line number')),
                ('revision_number', models.PositiveSmallIntegerField(help_text='Enter revision number')),
                ('order_quantity', models.PositiveSmallIntegerField(help_text='Enter order quantity')),
                ('unit_price', models.DecimalField(decimal_places=4, help_text='Enter unit price', max_digits=19)),
                ('extended_amount', models.DecimalField(decimal_places=4, help_text='Enter extended amount', max_digits=19)),
                ('unit_price_discount_pct', models.FloatField(help_text='Enter unit price discount percent')),
                ('discount_amount', models.FloatField(help_text='Enter discount amount')),
                ('product_standard_cost', models.DecimalField(decimal_places=4, help_text='Enter product standard cost', max_digits=19)),
                ('total_product_cost', models.DecimalField(decimal_places=4, help_text='Enter total product cost', max_digits=19)),
                ('sales_amount', models.DecimalField(decimal_places=4, help_text='Enter sales amount', max_digits=19)),
                ('tax_amt', models.DecimalField(decimal_places=4, help_text='Enter tax amount', max_digits=19)),
                ('freight', models.DecimalField(decimal_places=4, help_text='Enter freight', max_digits=19)),
                ('order_date_actual', models.DateTimeField(blank=True, help_text='Enter the actual order date', null=True)),
                ('due_date_actual', models.DateTimeField(blank=True, help_text='Enter the actual due date', null=True)),
                ('ship_date_actual', models.DateTimeField(blank=True, help_text='Enter the actual ship date', null=True)),
                ('currency', models.ForeignKey(help_text='Select currency for this sale', on_delete=django.db.models.deletion.RESTRICT, to='catalog.currency')),
                ('customer', models.ForeignKey(help_text='Select customer for this sale', on_delete=django.db.models.deletion.RESTRICT, to='catalog.customer')),
                ('due_date', models.ForeignKey(help_text='Select due date', on_delete=django.db.models.deletion.RESTRICT, related_name='orders_due_date', to='catalog.date')),
                ('order_date', models.ForeignKey(help_text='Select order date', on_delete=django.db.models.deletion.RESTRICT, related_name='orders_order_date', to='catalog.date')),
                ('product', models.ForeignKey(help_text='Select product for this sale', on_delete=django.db.models.deletion.RESTRICT, to='catalog.product')),
                ('promotions', models.ManyToManyField(blank=True, help_text='Select promotions for this order', to='catalog.promotion')),
                ('ship_date', models.ForeignKey(help_text='Select ship date', on_delete=django.db.models.deletion.RESTRICT, related_name='orders_ship_date', to='catalog.date')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'unique_together': {('sales_order_number', 'sales_order_line_number')},
            },
        ),
    ]