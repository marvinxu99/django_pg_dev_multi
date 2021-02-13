# Generated by Django 3.1.4 on 2021-01-15 04:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0029_auto_20210111_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueattachment',
            name='attachment',
            field=models.FileField(upload_to='itrac/'),
        ),
        migrations.AlterField(
            model_name='issueattachment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_issue', to='itrac.issue'),
        ),
        migrations.AlterField(
            model_name='issueattachment',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_uploader', to=settings.AUTH_USER_MODEL),
        ),
    ]
