# Generated by Django 5.1.2 on 2025-03-28 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IncomingItems',
            new_name='IncomingItem',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
