# Generated by Django 5.1.1 on 2024-10-14 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0010_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
