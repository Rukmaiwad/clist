# Generated by Django 3.1.12 on 2021-08-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0062_auto_20210828_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='long_contest_delay',
        ),
        migrations.AddField(
            model_name='module',
            name='long_contest_divider',
            field=models.IntegerField(default=12),
        ),
    ]