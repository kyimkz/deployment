# Generated by Django 5.0.2 on 2024-04-27 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='published', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=7, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='core.vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='title',
            field=models.CharField(default='Prava', max_length=100),
        ),
    ]
