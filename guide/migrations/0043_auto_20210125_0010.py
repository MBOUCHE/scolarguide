# Generated by Django 3.1.4 on 2021-01-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0042_auto_20210125_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='capacity',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='desc_inf',
            field=models.TextField(max_length=7),
        ),
    ]
