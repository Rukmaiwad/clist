# Generated by Django 4.2.3 on 2023-09-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0089_rename_resource_rank_account_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='country_rank',
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['resource', 'rank'], name='ranking_acc_resourc_65aa35_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['resource', '-rank'], name='ranking_acc_resourc_023f63_idx'),
        ),
    ]
