# Generated by Django 2.2 on 2022-07-09 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220709_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletas',
            name='expirationDate',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 21, 27, 2, 608358)),
        ),
    ]
