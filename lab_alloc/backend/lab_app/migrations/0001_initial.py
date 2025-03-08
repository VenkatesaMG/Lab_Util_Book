# Generated by Django 5.1.4 on 2025-03-08 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('lab_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=30, unique=True)),
                ('lab_capacity', models.IntegerField(default=5)),
                ('icon_name', models.CharField(max_length=20, null=True)),
                ('fallback_icon_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('main_reason', models.CharField(max_length=200)),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('hours', models.FloatField()),
                ('num_bookings', models.IntegerField()),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('date', 'lab_id'), name='daily_unique')],
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.TextField(max_length=25)),
                ('total_hours', models.FloatField()),
                ('num_bookings', models.IntegerField()),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('month', 'lab_id'), name='monthly_unique')],
            },
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schedule_date', models.DateField()),
                ('schedule_from', models.TimeField()),
                ('schedule_to', models.TimeField()),
                ('status', models.CharField(max_length=20, null=True)),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.user')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('username', 'lab_id', 'schedule_date', 'schedule_from', 'schedule_to'), name='unique_schedule_per_user_lab')],
            },
        ),
        migrations.CreateModel(
            name='ScheduleRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schedule_date', models.DateField()),
                ('schedule_from', models.TimeField()),
                ('schedule_to', models.TimeField()),
                ('status', models.CharField(default='pending', max_length=30)),
                ('decision_date', models.DateField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_app.admin')),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.user')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('username', 'lab_id', 'schedule_date', 'schedule_from', 'schedule_to', 'status'), name='unique_schedule_request')],
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('week_label', models.TextField(max_length=25)),
                ('week_num', models.IntegerField(blank=True, null=True)),
                ('total_hours', models.FloatField()),
                ('num_bookings', models.IntegerField()),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.laboratory')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('week_num', 'lab_id'), name='weekly_unique')],
            },
        ),
    ]
