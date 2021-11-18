# Generated by Django 3.2.9 on 2021-11-18 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eseven', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='eseven.Product')),
            ],
        ),
    ]
