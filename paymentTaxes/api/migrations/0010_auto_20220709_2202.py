# Generated by Django 2.2 on 2022-07-09 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220709_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletas',
            name='expirationDate',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 22, 2, 22, 396231)),
        ),
    ]