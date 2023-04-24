# Generated by Django 4.1 on 2022-08-23 18:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('next_allowed_update', models.DateTimeField(default=datetime.datetime(2022, 8, 23, 18, 44, 14, 986680))),
                ('location', models.CharField(default='none', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]