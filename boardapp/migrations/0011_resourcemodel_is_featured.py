# Generated by Django 2.2.6 on 2019-10-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0010_resourcemodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcemodel',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
