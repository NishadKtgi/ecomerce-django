# Generated by Django 5.1.2 on 2024-11-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shippingapp', '0005_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_confirm',
            name='order_id',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
