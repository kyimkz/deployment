# Generated by Django 5.0.2 on 2024-05-03 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cartorderitems_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylist',
            old_name='paid_status',
            new_name='liked',
        ),
    ]