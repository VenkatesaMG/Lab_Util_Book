# Generated by Django 5.1.4 on 2025-02-27 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='lab_id',
        ),
        migrations.AlterField(
            model_name='schedulerequest',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_app.admin'),
        ),
    ]
