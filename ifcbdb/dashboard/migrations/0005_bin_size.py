# Generated by Django 2.1.7 on 2019-03-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190329_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
