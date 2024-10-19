# Generated by Django 5.1.2 on 2024-10-19 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='workers.location'),
        ),
    ]
