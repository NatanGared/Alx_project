# Generated by Django 5.1.2 on 2025-03-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_alter_size_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='symbol',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
