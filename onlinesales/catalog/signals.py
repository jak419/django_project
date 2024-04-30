from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Orders, Product
from django.core.mail import send_mail
import csv
from pathlib import Path


# This handler logs a message whenever an order is created or updated
@receiver(post_save, sender=Orders)
def update_order_status(sender, instance, created, **kwargs):
    if created:
        print(f"New order created with ID: {instance.id}")
    else:
        print(f"Order updated with ID: {instance.id}")

# This logs a message right before a product is deleted


@receiver(pre_delete, sender=Product)
def product_pre_delete(sender, instance, **kwargs):
    print(f"Product to be deleted: {instance.english_product_name}")

# This handler sends an email notification to customer whenever an order is created or updated


@receiver(post_save, sender=Orders)
def update_order_status_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Order Confirmation',
            'Thank you for your order! Your order number is {}'.format(
                instance.id),
            'customerservice@marketplace.com',
            [instance.customer.email_address],
            fail_silently=False,
        )
    else:
        send_mail(
            'Order Updated',
            'Your order with number {} has been updated.'.format(instance.id),
            'customerservice@marketplace.com',
            [instance.customer.email_address],
            fail_silently=False,
        )


# This handler manages inventory after an order is placed
@receiver(post_save, sender=Orders)
def manage_inventory(sender, instance, **kwargs):
    product = instance.product
    product.inventory_count -= instance.order_quantity
    product.save()

# This handler logs in order_logs.csv when an order is placed


@receiver(post_save, sender=Orders)
def log_order_to_csv(sender, instance, created, **kwargs):
    file_path = Path(__file__).resolve().parent / "logs" / "orders_log.csv"
    print(f"Writing to {file_path}")

    with open(file_path, "a+", newline='') as csvfile:
        logwriter = csv.writer(csvfile, delimiter=',')
        logwriter.writerow([instance.id, instance.product.english_product_name,
                           instance.customer.first_name, instance.status, instance.order_date_actual])

    if created:
        print(f"New order created with ID: {instance.id}")
    else:
        print(f"Order updated with ID: {instance.id}")
