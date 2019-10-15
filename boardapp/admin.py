from django.contrib import admin
from .models import TeacherModel, RatingModel, ResourceModel, CommentModel
# Register your models here.

admin.site.register(TeacherModel)
admin.site.register(RatingModel)
admin.site.register(ResourceModel)
admin.site.register(CommentModel)