# Generated by Django 4.2.3 on 2023-09-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0112_alter_contest_standings_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='last_rating_update_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
