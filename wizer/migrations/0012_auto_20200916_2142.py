# Generated by Django 3.0.8 on 2020-09-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0011_auto_20200914_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uicacheactivitydata',
            name='altitude_list',
            field=models.CharField(default='[]', max_length=10000000000, null=True),
        ),
    ]
