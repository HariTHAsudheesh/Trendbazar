# Generated by Django 5.0.1 on 2024-03-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_basket_owner_alter_basketitem_basket_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
    ]
