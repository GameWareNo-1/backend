# Generated by Django 5.1.4 on 2025-01-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_alter_levelscore_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
            options={
                'unique_together': {('username', 'level')},
            },
        ),
        migrations.DeleteModel(
            name='LevelScore',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
