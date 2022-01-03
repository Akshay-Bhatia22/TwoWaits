# Generated by Django 3.2.10 on 2021-12-28 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('college', models.CharField(blank=True, max_length=50, null=True)),
                ('course', models.CharField(blank=True, choices=[('BTECH', 'BTECH'), ('MTECH', 'MTECH'), ('BCA', 'BCA'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('BBA', 'BBA'), ('BA', 'BA'), ('MA', 'MA')], max_length=10, null=True)),
                ('branch', models.CharField(blank=True, choices=[('CS', 'Computer Science'), ('CS&IT', 'Computer Science and IT'), ('IT', 'IT'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('EE', 'Electrical and Electronics'), ('Humanities', 'Humanities'), ('Others', 'Any other')], max_length=10, null=True)),
                ('year', models.CharField(blank=True, choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4th year')], max_length=1, null=True)),
                ('interest', models.CharField(blank=True, choices=[('Job', 'Job'), ('GATE', 'GATE'), ('GRE', 'GRE'), ('CAT', 'CAT'), ('MBA', 'MBA'), ('MS', 'MS')], max_length=15, null=True)),
                ('profile_pic', models.ImageField(default='ProfilePic/Avatar1.png', upload_to='ProfilePic')),
                ('student_account_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
