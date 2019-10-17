from django.db import models
from django.utils import timezone
# Create your models here.

sub_choices = (
    ('maths','Maths'),
    ('science','Science'),
    ('english','English'),
)

lev_choices = (
    ('1st','1st Year'),
    ('2nd','2nd Year'),
)

topic_choices = (
    ('fractions','Fractions'),
    ('algebra','Algebra'),
    ('vocabulary','Vocabulary'),
)

class TeacherModel(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    followed_by = models.ManyToManyField("self", related_name='following',blank=True)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class SubjectModel(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class LevelModel(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class TopicModel(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ResourceModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, related_name='resources', on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    description = models.TextField(max_length=2000, null=True)
    subject = models.ForeignKey(SubjectModel, related_name='subject_resources', on_delete = models.CASCADE)
    level = models.ForeignKey(LevelModel, related_name='level_resources', on_delete=models.CASCADE)
    topic = models.ForeignKey(TopicModel, related_name='topic_resources', on_delete=models.CASCADE)
    saved_by = models.ManyToManyField(TeacherModel, related_name='saved_resources', blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.link


class RatingModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='ratings', on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, related_name='given_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.resource.link


class CommentModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='comments',on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, related_name='given_comments',on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now, blank =True, null=True)


    def __str__(self):
        return self.comment

