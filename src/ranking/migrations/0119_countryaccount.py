# Generated by Django 4.2.11 on 2024-04-05 23:04

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0141_problem_skip_rating'),
        ('ranking', '0118_stagecontest_created_stagecontest_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('country', django_countries.fields.CountryField(db_index=True, max_length=2)),
                ('n_accounts', models.IntegerField(db_index=True, default=0)),
                ('rating', models.IntegerField(blank=True, db_index=True, default=None, null=True)),
                ('rating50', models.SmallIntegerField(blank=True, db_index=True, default=None, null=True)),
                ('resource_rank', models.IntegerField(blank=True, db_index=True, default=None, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clist.resource')),
            ],
            options={
                'indexes': [models.Index(fields=['resource', 'country'], name='ranking_cou_resourc_680ff7_idx'), models.Index(fields=['resource', 'rating'], name='ranking_cou_resourc_057da3_idx'), models.Index(fields=['resource', '-rating'], name='ranking_cou_resourc_9b17d0_idx'), models.Index(fields=['resource', 'rating50'], name='ranking_cou_resourc_34b7c7_idx'), models.Index(fields=['resource', '-rating50'], name='ranking_cou_resourc_4fdb9f_idx'), models.Index(fields=['resource', 'resource_rank'], name='ranking_cou_resourc_0531f0_idx'), models.Index(fields=['resource', '-resource_rank'], name='ranking_cou_resourc_fe9631_idx'), models.Index(fields=['resource', 'n_accounts'], name='ranking_cou_resourc_96dbbb_idx'), models.Index(fields=['resource', '-n_accounts'], name='ranking_cou_resourc_977a09_idx'), models.Index(fields=['resource', 'country', 'rating'], name='ranking_cou_resourc_e55400_idx'), models.Index(fields=['resource', 'country', '-rating'], name='ranking_cou_resourc_f1ec91_idx'), models.Index(fields=['resource', 'country', 'rating50'], name='ranking_cou_resourc_81baef_idx'), models.Index(fields=['resource', 'country', '-rating50'], name='ranking_cou_resourc_18a92d_idx'), models.Index(fields=['resource', 'country', 'resource_rank'], name='ranking_cou_resourc_b6db42_idx'), models.Index(fields=['resource', 'country', '-resource_rank'], name='ranking_cou_resourc_504afb_idx'), models.Index(fields=['resource', 'country', 'n_accounts'], name='ranking_cou_resourc_7144e9_idx'), models.Index(fields=['resource', 'country', '-n_accounts'], name='ranking_cou_resourc_e33742_idx')],
            },
        ),
    ]
