# Generated by Django 3.0.8 on 2020-10-22 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201021_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': (('can_load_shop_data', 'can load shop data'), ('can_delete_shop_data', 'can delete shop data'))},
        ),
    ]