# Generated by Django 2.2 on 2019-04-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_service_data_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_data',
            name='posi',
            field=models.CharField(default='', max_length=50),
        ),
    ]
