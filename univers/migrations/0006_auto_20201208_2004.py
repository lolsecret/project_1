# Generated by Django 3.1.3 on 2020-12-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0005_auto_20201208_1954'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.RemoveField(
            model_name='groupspec',
            name='graduate_date',
        ),
        migrations.AlterField(
            model_name='groupspec',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
