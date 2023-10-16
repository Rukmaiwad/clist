# Generated by Django 4.2.3 on 2023-10-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logify', '0004_alter_eventlog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlog',
            name='status',
            field=models.CharField(choices=[('default', 'Default'), ('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('in_progress', 'In Progress'), ('cancelled', 'Cancelled'), ('on_hold', 'On Hold'), ('initiated', 'Initiated'), ('reviewed', 'Reviewed'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('archived', 'Archived'), ('deleted', 'Deleted'), ('skipped', 'Skipped'), ('reverted', 'Reverted'), ('exception', 'Exception')], db_index=True, default='default', max_length=20),
        ),
    ]
