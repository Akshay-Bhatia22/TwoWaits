# Generated by Django 3.2.10 on 2022-01-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0004_file_file_obj_firebase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_obj',
            field=models.FileField(blank=True, null=True, upload_to='Note_files'),
        ),
    ]
