# Generated by Django 3.0.3 on 2020-07-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0001_squashed_0036_auto_20200629_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='trigger',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='settings',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='traces',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
