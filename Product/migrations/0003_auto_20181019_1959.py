# Generated by Django 2.0.4 on 2018-10-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catName',
            field=models.CharField(max_length=20),
        ),
    ]
