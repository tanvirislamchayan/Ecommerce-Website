# Generated by Django 5.0.4 on 2024-06-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_cartitems_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
