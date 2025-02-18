# Generated by Django 5.1.4 on 2024-12-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.PositiveIntegerField(help_text='Time in seconds')),
                ('materials', models.JSONField(help_text='List of material codes')),
                ('target', models.JSONField(help_text='Target dictionary for materials')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
