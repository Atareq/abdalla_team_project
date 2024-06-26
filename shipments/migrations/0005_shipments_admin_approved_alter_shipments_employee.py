# Generated by Django 5.0.6 on 2024-06-19 14:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_shipments_quentity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shipments',
            name='admin_approved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_shipments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shipments',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_shipments', to=settings.AUTH_USER_MODEL),
        ),
    ]
