# Generated by Django 4.2.11 on 2024-03-31 11:14

from django.db import migrations, models
import django.db.models.deletion


def set_new_stage_contest(apps, schema_editor):
    Stage = apps.get_model('ranking', 'Stage')
    for stage in Stage.objects.all():
        for contest in stage.contests.all():
            stage.new_contests.add(contest)


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0141_problem_skip_rating'),
        ('ranking', '0113_alter_rating_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clist.contest')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.stage')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='new_contests',
            field=models.ManyToManyField(blank=True, related_name='new_stages', through='ranking.StageContest', to='clist.contest'),
        ),

        migrations.RunPython(set_new_stage_contest),
    ]