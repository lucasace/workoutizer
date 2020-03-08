# Generated by Django 2.2.5 on 2020-03-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0004_auto_20200223_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traces',
            old_name='heart_rate',
            new_name='heart_rate_list',
        ),
        migrations.AlterField(
            model_name='settings',
            name='number_of_days',
            field=models.IntegerField(choices=[(9999, 'all'), (365, 365), (180, 180), (90, 90), (30, 30), (10, 10)], default=30),
        ),
    ]
