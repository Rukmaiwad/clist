# Generated by Django 3.1.14 on 2022-01-10 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0022_auto_20220110_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificationmessage',
            options={'verbose_name': 'Message'},
        ),
    ]