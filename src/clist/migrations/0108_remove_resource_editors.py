# Generated by Django 3.1.14 on 2023-07-22 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0107_auto_20230722_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='editors',
        ),
    ]