# Generated by Django 5.1.4 on 2025-01-14 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_app', '0004_user_remove_schedules_user_id_schedules_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('lab_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='schedules',
            name='lab_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='schedules',
            constraint=models.UniqueConstraint(fields=('username', 'lab_id', 'schedule_date', 'schedule_from', 'schedule_to'), name='unique_schedule_per_user_lab'),
        ),
    ]
