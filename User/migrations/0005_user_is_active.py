# Generated by Django 2.0.4 on 2018-11-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_email_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Active',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]