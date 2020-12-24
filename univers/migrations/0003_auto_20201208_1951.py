# Generated by Django 3.1.3 on 2020-12-08 13:51

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0002_auto_20201208_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupspec',
            name='test',
            field=models.UUIDField(default=uuid.UUID('bf36e4b1-038a-4556-b32e-569be75fbce0')),
        ),
        migrations.AlterField(
            model_name='groupspec',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
