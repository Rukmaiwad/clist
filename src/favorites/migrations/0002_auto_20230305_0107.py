# Generated by Django 3.1.14 on 2023-03-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('fav', 'Favorite'), ('lik', 'Like'), ('sol', 'Solved'), ('rej', 'Reject'), ('tdo', 'Todo')], max_length=3),
        ),
    ]