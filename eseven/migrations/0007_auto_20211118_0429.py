# Generated by Django 3.2.9 on 2021-11-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eseven', '0006_alter_order_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='admin_revenue',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='ambassador_revenue',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
