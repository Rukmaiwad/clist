# Generated by Django 2.2.10 on 2020-03-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0029_resource_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='has_rating_history',
            field=models.BooleanField(default=False),
        ),
    ]