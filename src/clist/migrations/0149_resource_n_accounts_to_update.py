# Generated by Django 4.2.11 on 2024-05-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0148_contest_has_submissions_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='n_accounts_to_update',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
