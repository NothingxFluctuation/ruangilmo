# Generated by Django 2.2.6 on 2019-10-18 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('student', 'student'), ('teacher', 'teacher')], max_length=50, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TopicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('followed_by', models.ManyToManyField(blank=True, related_name='_teachermodel_followed_by_+', to='boardapp.TeacherModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching', to='boardapp.ProfileModel')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_resources', to='boardapp.LevelModel')),
                ('saved_by', models.ManyToManyField(blank=True, related_name='saved_resources', to='boardapp.TeacherModel')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_resources', to='boardapp.SubjectModel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='boardapp.TeacherModel')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_resources', to='boardapp.TopicModel')),
            ],
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='boardapp.ResourceModel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_ratings', to='boardapp.TeacherModel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boardapp.ResourceModel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_comments', to='boardapp.TeacherModel')),
            ],
        ),
    ]
