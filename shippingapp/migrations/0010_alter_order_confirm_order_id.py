# Generated by Django 5.1.2 on 2024-11-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shippingapp', '0009_alter_order_confirm_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_confirm',
            name='order_id',
            field=models.CharField(max_length=50),
        ),
    ]
