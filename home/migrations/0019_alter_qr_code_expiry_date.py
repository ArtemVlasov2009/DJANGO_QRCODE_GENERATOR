# Generated by Django 3.2.19 on 2025-03-05 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_qr_code_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 4, 19, 38, 48, 574102, tzinfo=utc)),
        ),
    ]
