# Generated by Django 3.1.4 on 2020-12-26 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_arrondissement_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrondissement',
            name='department',
        ),
    ]