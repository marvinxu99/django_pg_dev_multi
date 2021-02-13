# Generated by Django 3.0.7 on 2020-08-22 05:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0020_auto_20200821_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
