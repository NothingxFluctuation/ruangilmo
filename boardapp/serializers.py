from rest_framework import serializers
from .models import TeacherModel, ResourceModel, RatingModel, CommentModel, ProfileModel, TopicModel, LevelModel, SubjectModel



#serializers

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id','user','role','created')

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ('id','user','followed_by','is_admin','created')


class ResourceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceModel
        fields = ('id','author','link','description','subject','level','topic','resource_type','saved_by','created')


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = ('id','resource','rated_by','rating','created')


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id','resource','commenter','comment','created')


class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = ('id','title','level','subject','created')

class LevelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelModel
        fields = ('id','title','subject','created')

class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = ('id','title','created')

