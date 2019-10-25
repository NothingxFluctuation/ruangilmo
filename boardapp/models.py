from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

m_role = (
    ('student','student'),
    ('teacher','teacher'),
)


class ProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices = m_role, null=True, blank=True, default='student')
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.user.username





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
    user = models.ForeignKey(ProfileModel, related_name='teaching', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    followed_by = models.ManyToManyField(User, related_name='following',blank=True, default='')
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.user.user.username

class StudentModel(models.Model):
    user = models.ForeignKey(ProfileModel, related_name='studying', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.user.user.username

class IsStudentAllowedToPost(models.Model):
    Allowed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Allowed)



class SubjectModel(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

class LevelModel(models.Model):
    title = models.CharField(max_length=250)
    subject = models.ForeignKey(SubjectModel, blank=True, null=True, related_name='subject_levels', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

class TopicModel(models.Model):
    title = models.CharField(max_length=250)
    level = models.ForeignKey(LevelModel, blank=True, null=True, related_name='level_topics', on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, blank=True, null=True, related_name='subject_topics', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title


notex_choices = (
    ('exercise','Exercise'),
    ('notes','Notes'),
)



class ResourceModel(models.Model):
    author = models.ForeignKey(ProfileModel, related_name='resources', on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=1000)
    description = models.TextField(max_length=2000, null=True)
    subject = models.ForeignKey(SubjectModel, related_name='subject_resources', on_delete = models.CASCADE)
    level = models.ForeignKey(LevelModel, related_name='level_resources', on_delete=models.CASCADE)
    topic = models.ForeignKey(TopicModel, related_name='topic_resources', on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=50, choices = notex_choices, default='exercise', blank=True, null=True)
    saved_by = models.ManyToManyField(User, related_name='saved_resources', blank=True, default='')
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.link


class RatingModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='ratings', on_delete=models.CASCADE)
    rated_by = models.ForeignKey(ProfileModel, related_name='given_ratings', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.resource.link


class CommentModel(models.Model):
    resource = models.ForeignKey(ResourceModel, related_name='comments',on_delete=models.CASCADE)
    commenter = models.ForeignKey(ProfileModel, related_name='given_comments',on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now, blank =True, null=True)


    def __str__(self):
        return self.comment

