# Generated by Django 2.2.6 on 2019-10-21 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0012_auto_20191019_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='disabled',
        ),
    ]
