# Generated by Django 2.0.4 on 2018-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('catId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('catName', models.CharField(max_length=10)),
                ('catImg', models.ImageField(upload_to='img/category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]