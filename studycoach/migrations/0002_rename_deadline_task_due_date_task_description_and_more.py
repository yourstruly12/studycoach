# Generated by Django 5.2 on 2025-04-07 21:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studycoach', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='deadline',
            new_name='due_date',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
