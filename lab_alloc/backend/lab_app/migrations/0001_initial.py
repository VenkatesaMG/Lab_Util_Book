# Generated by Django 5.1.4 on 2025-01-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('schedule_date', models.DateField()),
                ('schedule_from', models.TimeField()),
                ('schedule_to', models.TimeField()),
            ],
        ),
    ]
