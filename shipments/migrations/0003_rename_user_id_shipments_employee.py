# Generated by Django 5.0.6 on 2024-06-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipments',
            old_name='user_id',
            new_name='employee',
        ),
    ]