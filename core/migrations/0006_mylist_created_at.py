# Generated by Django 5.0.2 on 2024-05-07 12:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mylist_paid_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]