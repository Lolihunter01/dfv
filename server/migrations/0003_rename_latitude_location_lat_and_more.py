# Generated by Django 4.0.6 on 2022-07-11 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_delete_his_alter_location_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='lontitude',
            new_name='lon',
        ),
    ]
