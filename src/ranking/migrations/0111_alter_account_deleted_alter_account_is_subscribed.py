# Generated by Django 4.2.3 on 2023-12-20 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0110_account_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='deleted',
            field=models.BooleanField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_subscribed',
            field=models.BooleanField(blank=True, db_index=True, default=None, null=True),
        ),
    ]