# Generated by Django 3.1.4 on 2021-01-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0039_auto_20210121_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='appart',
            name='last_modify_apt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
