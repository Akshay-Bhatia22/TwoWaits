# Generated by Django 3.2.10 on 2022-01-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_remove_correctoption_correct_option_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
