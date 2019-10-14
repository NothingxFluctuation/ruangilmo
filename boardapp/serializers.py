from rest_framework import serializers
from .models import TeacherModel, ResourceModel, RatingModel, CommentModel



#serializers

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ('id','name','created')
    

class ResourceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceModel
        fields = ('teacher','link','subject','level','topic','saved_by','created')


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = ('resource','teacher','rating','created')


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('resource','teacher','comment','created')


