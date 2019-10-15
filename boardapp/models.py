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

    def __str__(self):
        return self.name



class ResourceModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, related_name='resources', on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    subject = models.CharField(max_length=50,choices=sub_choices)
    level = models.CharField(max_length=50, choices=lev_choices)
    topic = models.CharField(max_length=50, choices=topic_choices)
    saved_by = models.ManyToManyField(TeacherModel, related_name='saved_resources', blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.link


class RatingModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='ratings', on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, related_name='given_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.resource


class CommentModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='comments',on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, related_name='given_comments',on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now, blank =True, null=True)


    def __str__(self):
        return self.comment

