# Generated by Django 2.2 on 2019-05-13 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_content_file_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_data',
            old_name='charge',
            new_name='ppp',
        ),
        migrations.RenameField(
            model_name='service_data',
            old_name='posi',
            new_name='ssl',
        ),
    ]