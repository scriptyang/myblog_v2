# Generated by Django 2.2 on 2019-04-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_data',
            name='charge',
            field=models.CharField(default='', max_length=50),
        ),
    ]
