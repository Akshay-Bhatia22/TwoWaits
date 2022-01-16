# Generated by Django 3.2.10 on 2022-01-16 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_results', '0003_rename_response_studentresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('total_questions', models.IntegerField()),
                ('attempted', models.IntegerField()),
                ('correct', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('total_score', models.CharField(max_length=10)),
                ('quiz_result_score_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_result_score', to='Quiz_results.quizresult')),
            ],
        ),
    ]