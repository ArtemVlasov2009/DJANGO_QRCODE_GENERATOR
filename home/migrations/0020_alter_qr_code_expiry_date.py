# Generated by Django 3.2.19 on 2025-03-05 19:40

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_qr_code_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='expiry_date',
            field=models.FloatField(default=time.time),
        ),
    ]
