from django.shortcuts import render
from rest_framework import viewsets
from .models import TeacherModel, ResourceModel, RatingModel, CommentModel
from .serializers import TeacherModelSerializer, ResourceModelSerializer, RatingModelSerializer, CommentModelSerializer


# Create your views here.

class TeacherModelViewset(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherModelSerializer



class ResourceModelViewset(viewsets.ModelViewSet):
    queryset = ResourceModel.objects.all()
    serializer_class = ResourceModelSerializer

class RatingModelViewset(viewsets.ModelViewSet):
    queryset = RatingModel.objects.all()
    serializer_class = RatingModelSerializer

class CommentModelViewset(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer


