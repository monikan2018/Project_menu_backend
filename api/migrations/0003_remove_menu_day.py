# Generated by Django 3.0 on 2020-09-19 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200916_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='day',
        ),
    ]
