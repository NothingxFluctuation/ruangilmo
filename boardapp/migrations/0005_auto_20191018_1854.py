# Generated by Django 2.2.6 on 2019-10-18 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_auto_20191018_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcemodel',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='saved_resources', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='followed_by',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('disabled', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studying', to='boardapp.ProfileModel')),
            ],
        ),
    ]
