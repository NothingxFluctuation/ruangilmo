from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import TeacherModel, ResourceModel, RatingModel, CommentModel
from .serializers import TeacherModelSerializer, ResourceModelSerializer, RatingModelSerializer, CommentModelSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

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

@api_view()
def get_resources(request):
    if request.method =='GET':
        resources = ResourceModel.objects.all()
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data)

@api_view()
def get_teachers(request):
    if request.method == 'GET':
        teachers = TeacherModel.objects.all()
        serializer = TeacherModelSerializer(teachers, many = True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def create_resource(request):
    if request.method =='GET':
        resources = ResourceModel.objects.all()
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data)




    elif request.method =='POST':
        serializer = ResourceModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_create_ratings(request):
    if request.method == 'GET':
        rv = request.GET.get('rsc_id')
        rsc_filter = ResourceModel.objects.filter(id=rv)
        if len(rsc_filter) > 0:
            rsc_obj = ResourceModel.objects.get(id=rv)
            ratings = RatingModel.objects.filter(resource = rsc_obj)
            serializer = RatingModelSerializer(ratings, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        
    elif request.method == 'POST':
        serializer = RatingModelSerializer(data = request.data)
        rsc_i = request.POST.get('resource')
        tch_i = request.POST.get('teacher')
        rating = request.POST.get('rating')
        rat_f = RatingModel.objects.filter(resource=rsc_i, teacher=tch_i)
        update = False
        if len(rat_f) >= 0:
            update = True
        if serializer.is_valid():
            if update:
                rat_old = RatingModel.objects.get(resource=rsc_i, teacher=tch_i)
                rat_old.rating = rating
                rat_old.save()
                serializer = RatingModelSerializer(rat_old)
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            else:
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
def get_create_comments(request):
    if request.method == 'GET':
        rv = request.GET.get('rsc_id')
        rsc_filter = ResourceModel.objects.filter(id=rv)
        if len(rsc_filter) > 0:
            rsc_obj = ResourceModel.objects.get(id=rv)
            comments = CommentModel.objects.filter(resource = rsc_obj)
            serializer = CommentModelSerializer(comments, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = CommentModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def un(request):
    return render(request,'un.html')