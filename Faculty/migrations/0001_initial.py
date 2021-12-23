# Generated by Django 3.2.9 on 2021-12-20 16:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('college', models.CharField(blank=True, max_length=40, null=True)),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('qualification', models.CharField(choices=[('P', 'Postgraduate'), ('U', 'Undergraduate')], max_length=10)),
                ('profile_pic', models.ImageField(default='ProfilePic/Avatar1.png', upload_to='ProfilePic')),
                ('faculty_account_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]