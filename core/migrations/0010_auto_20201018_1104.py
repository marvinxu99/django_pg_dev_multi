# Generated by Django 3.0.8 on 2020-10-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201018_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevalue',
            name='inactivate_dt_tm',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
