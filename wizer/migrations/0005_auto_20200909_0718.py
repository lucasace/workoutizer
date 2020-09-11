# Generated by Django 3.0.8 on 2020-09-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0004_traces_distance_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='UICacheActivityData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='aerobic_training_effect',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='anaerobic_training_effect',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]