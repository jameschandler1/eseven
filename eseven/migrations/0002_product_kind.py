# Generated by Django 3.2.9 on 2021-12-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eseven', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
