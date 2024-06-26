# Generated by Django 4.2.11 on 2024-05-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0020_submission_current_attempt'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'contest_time'], name='submissions_contest_bfe680_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', '-contest_time'], name='submissions_contest_88eae4_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'account', 'contest_time'], name='submissions_contest_e0f97b_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'account', '-contest_time'], name='submissions_contest_b8bfe4_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'problem_short', 'contest_time'], name='submissions_contest_691edf_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'problem_short', '-contest_time'], name='submissions_contest_8be12d_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'account', 'problem_short', 'contest_time'], name='submissions_contest_e40630_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['contest', 'account', 'problem_short', '-contest_time'], name='submissions_contest_f9cdc5_idx'),
        ),
    ]
