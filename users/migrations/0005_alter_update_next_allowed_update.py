# Generated by Django 4.1 on 2022-08-23 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_update_next_allowed_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='next_allowed_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 19, 4, 52, 234271)),
        ),
    ]
