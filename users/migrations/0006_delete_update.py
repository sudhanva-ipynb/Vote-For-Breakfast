# Generated by Django 4.1 on 2022-08-23 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_update_next_allowed_update'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Update',
        ),
    ]