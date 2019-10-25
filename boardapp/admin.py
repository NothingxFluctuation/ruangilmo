from django.contrib import admin
from .models import TeacherModel, RatingModel, ResourceModel, CommentModel, SubjectModel, TopicModel, LevelModel, StudentModel, ProfileModel,\
    IsStudentAllowedToPost
# Register your models here.

admin.site.register(TeacherModel)
admin.site.register(RatingModel)
admin.site.register(ResourceModel)
admin.site.register(CommentModel)
admin.site.register(SubjectModel)
admin.site.register(TopicModel)
admin.site.register(LevelModel)
admin.site.register(ProfileModel)
admin.site.register(StudentModel)
admin.site.register(IsStudentAllowedToPost)