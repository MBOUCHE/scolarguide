# Generated by Django 3.1.4 on 2020-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0025_auto_20201227_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='s_std',
        ),
        migrations.AddField(
            model_name='detail',
            name='birth_paper',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SpecialStudent',
        ),
    ]