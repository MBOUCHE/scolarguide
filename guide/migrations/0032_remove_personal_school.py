# Generated by Django 3.1.4 on 2020-12-29 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0031_auto_20201229_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='school',
        ),
    ]
