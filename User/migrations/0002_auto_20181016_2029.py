# Generated by Django 2.0.4 on 2018-10-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uSex',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
