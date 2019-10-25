# Generated by Django 2.2.6 on 2019-10-23 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0015_auto_20191023_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelmodel',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_levels', to='boardapp.SubjectModel'),
        ),
        migrations.AlterField(
            model_name='topicmodel',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_topics', to='boardapp.LevelModel'),
        ),
    ]