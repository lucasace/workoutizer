# Generated by Django 2.2.5 on 2020-01-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0047_auto_20191212_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='traces',
            name='heart_rate',
            field=models.CharField(blank=True, max_length=10000000000, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='map_type',
            field=models.CharField(choices=[('osm', 'Open Street Map'), ('opentopomap', 'Open Topo Map')], default='osm', max_length=120, verbose_name='Map Type:'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='path_to_garmin_device',
            field=models.CharField(default='/run/user/1000/gvfs/', max_length=120, verbose_name='Path to Garmin Device:'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='path_to_trace_dir',
            field=models.CharField(default='/home/pi/traces/', max_length=120, verbose_name='Path to Traces Directory:'),
        ),
    ]
