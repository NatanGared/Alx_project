# Generated by Django 5.1.2 on 2025-03-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_rename_full_name_supplier_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='item',
        ),
        migrations.AddField(
            model_name='size',
            name='description',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='size',
            name='symbol',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
