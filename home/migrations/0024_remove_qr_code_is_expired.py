# Generated by Django 3.2.19 on 2025-03-06 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_qr_code_is_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr_code',
            name='is_expired',
        ),
    ]
