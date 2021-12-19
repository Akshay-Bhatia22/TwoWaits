# Generated by Django 4.0 on 2021-12-19 06:24

import Accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expiry',
            field=models.DateTimeField(default=Accounts.models.OTP.expiry),
        ),
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='otp',
            name='otp_account_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to='Accounts.useraccount'),
        ),
    ]
