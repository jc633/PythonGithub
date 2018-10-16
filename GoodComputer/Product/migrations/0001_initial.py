# Generated by Django 2.0.4 on 2018-10-15 13:32

import Product.listfield
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('proId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=20)),
                ('proPrice', models.CharField(max_length=10)),
                ('proStock', models.CharField(max_length=10)),
                ('proSale', models.BooleanField()),
                ('proHot', models.BooleanField()),
                ('proRmark', models.CharField(max_length=20)),
                ('proTrade', models.CharField(max_length=20)),
                ('proBrand', models.CharField(max_length=10)),
                ('proSeries', models.CharField(max_length=10)),
                ('proDesc', models.CharField(max_length=30)),
                ('proShopId', models.CharField(max_length=20)),
                ('proShopName', models.CharField(max_length=20)),
                ('proImg', Product.listfield.ListField()),
                ('proTime', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('shopId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shopName', models.CharField(max_length=20)),
                ('shopOwner', models.CharField(max_length=20)),
                ('shopHoner', models.IntegerField()),
                ('shopNotice', models.IntegerField()),
                ('shopDesc', models.CharField(max_length=30, null=True)),
                ('shopImg', models.ImageField(upload_to='img/shop/')),
                ('shopTime', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'shop',
            },
        ),
    ]
