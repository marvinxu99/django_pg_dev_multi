# Generated by Django 3.0.7 on 2020-07-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itrac', '0002_auto_20200713_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('01', 'Break/fix'), ('02', 'New feature'), ('03', 'Optimization')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('01', 'Open'), ('02', 'Investigate'), ('03', 'Await approval'), ('04', 'Build in progress'), ('05', 'Validate in progress'), ('06', 'Complete'), ('07', 'Closed')], default='01', max_length=2),
        ),
    ]